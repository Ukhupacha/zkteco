#!/usr/bin/python3
import uvicorn
import argparse
import matplotlib
import matplotlib.pyplot as plt
import locale
import base64
import io
from typing import Optional
from datetime import date
from utils import *
from pathlib import Path
from fastapi import FastAPI, Request, Form
from starlette.templating import Jinja2Templates
from starlette.responses import FileResponse

sys.path.append("zk")

locale.setlocale(locale.LC_ALL, 'es_ES.UTF-8')
BASE_DIR = Path(__file__).resolve().parent
templates = Jinja2Templates(directory=str(Path(BASE_DIR, 'templates')))

app = FastAPI()
zk = ZK('zkteco.intranet', port=4370, timeout=5, password=0, force_udp=False, ommit_ping=False)
user_list = get_user_list(zk)
image_path = 'image.png'
matplotlib.use('agg')


# Dependency
@app.get("/")
def home(request: Request):
    return templates.TemplateResponse("base.html",
                                      {"request": request, "user_list": user_list})


@app.post("/pdf")
def generate_report(request: Request, start_date: date = Form(...), end_date: Optional[date] = Form(None)):
    start_date = datetime(start_date.year, start_date.month, start_date.day)
    end_date = datetime(end_date.year, end_date.month, end_date.day)
    attendance = filter_by_date(zk, user_list, start_date, end_date)
    users_history = attendance_to_dict(attendance)
    worked = count_days(users_history, 0)
    pdf = create_pdf(users_history, worked, user_list, start_date, end_date)
    pdf_temp = "attendance.pdf"
    pdf.output(pdf_temp)
    name = "report.pdf"

    return FileResponse(pdf_temp, media_type="application/pdf", filename=name)


@app.post("/attendance")
async def attendance_image(request: Request, id_worker: int = Form(...), start_date: date = Form(...),
                           end_date: date = Form(...), day_wage: int = Form(...)):
    user = [id_worker]
    start_date = datetime(start_date.year, start_date.month, start_date.day)
    end_date = datetime(end_date.year, end_date.month, end_date.day)
    attendance = filter_by_date(zk, user, start_date, end_date)
    user_history = attendance_to_dict(attendance)
    dates, data, days, errors = data_to_july(user_history, start_date, end_date)

    axes = create_july_image(dates, data, days, errors, day_wage)
    fig = axes.get_figure()
    plt.axes(axes)
    img_buf = io.BytesIO()
    plt.savefig(img_buf, format='PNG')
    plt.close(fig)
    png = img_buf.getvalue()
    img_buf.close()
    base64_encoded_image = base64.b64encode(png).decode("utf-8")
    title = [user_list[id_worker], start_date.strftime("%d/%m/%y") + " - " + end_date.strftime("%d/%m/%y")]
    return templates.TemplateResponse("base.html",
                                      {"request": request,
                                       "user_list": user_list,
                                       "title": title,
                                       "img": base64_encoded_image})


if __name__ == "__main__":
    parser = argparse.ArgumentParser(description='Attendance app')
    parser.add_argument('-a', '--address', help='Host address', default='0.0.0.0')
    parser.add_argument('-p', '--port', type=int, help='Host port', default=80)

    args = parser.parse_args()
    uvicorn.run(app, host=args.address, port=args.port)
