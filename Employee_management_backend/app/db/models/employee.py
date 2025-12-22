import datetime as dt
from sqlalchemy import String, Date, DateTime
from sqlalchemy.orm import Mapped, mapped_column
from fastapi_employee_management.db.base import Base

class Employee(Base):
    __tablename__ = "employee"

    employee_id: Mapped[int] = mapped_column(primary_key=True)
    first_name: Mapped[str] = mapped_column(String(), nullable=False)
    last_name: Mapped[str] = mapped_column(String(), nullable=False)
    email_id: Mapped[str | None] = mapped_column(String())
    blood_group: Mapped[str | None] = mapped_column(String())
    gender_val_txt: Mapped[str | None] = mapped_column(String())
    date_of_birth_val: Mapped[dt.date] = mapped_column(Date, nullable=False)
    marital_status: Mapped[str | None] = mapped_column(String())
    street_address: Mapped[str | None] = mapped_column(String())
    city: Mapped[str | None] = mapped_column(String())
    state: Mapped[str | None] = mapped_column(String())
    postal_code: Mapped[str | None] = mapped_column(String())
    country: Mapped[str | None] = mapped_column(String())
    phone_number: Mapped[str | None] = mapped_column(String())
    department_id: Mapped[int | None] = mapped_column()
    designation: Mapped[str | None] = mapped_column(String())
    role_nm: Mapped[str | None] = mapped_column(String())
    hire_date: Mapped[dt.date | None] = mapped_column(Date, nullable=False)
    employment_status: Mapped[str | None] = mapped_column(String(), nullable=False)
    employee_type: Mapped[str | None] = mapped_column(String())
    probation_ended_at: Mapped[dt.date | None] = mapped_column(Date)
    created_at: Mapped[dt.datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    updated_at: Mapped[dt.datetime] = mapped_column(DateTime(timezone=True), nullable=False)
    updated_by: Mapped[str | None] = mapped_column(String())
    cognite_sub: Mapped[str | None] = mapped_column(String())
    manager_employee_: Mapped[int | None] = mapped_column()
    campus_id: Mapped[int | None] = mapped_column()
