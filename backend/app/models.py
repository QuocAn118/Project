from sqlalchemy import Column, Integer, String, ForeignKey, DateTime, Text, Enum, Float
from sqlalchemy.orm import relationship
from sqlalchemy.sql import func
from .database import Base
import enum

class RoleEnum(str, enum.Enum):
    admin = "admin"
    manager = "manager"
    staff = "staff"

class StatusEnum(str, enum.Enum):
    available = "available"
    busy = "busy"
    offline = "offline"

class Department(Base):
    __tablename__ = "departments"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String, unique=True, index=True)
    users = relationship("User", back_populates="department")

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True, index=True)
    username = Column(String, unique=True, index=True)
    full_name = Column(String)
    hashed_password = Column(String)
    role = Column(Enum(RoleEnum), default=RoleEnum.staff)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=True)
    department = relationship("Department", back_populates="users")
    kpi_score = Column(Float, default=0.0)
    status = Column(Enum(StatusEnum), default=StatusEnum.available)

class Keyword(Base):
    __tablename__ = "keywords"
    id = Column(Integer, primary_key=True, index=True)
    word = Column(String, unique=True, index=True)
    department_id = Column(Integer, ForeignKey("departments.id"), nullable=True)
    department = relationship("Department")

class Message(Base):
    __tablename__ = "messages"
    id = Column(Integer, primary_key=True, index=True)
    platform = Column(String)
    sender = Column(String, index=True)
    content = Column(Text)
    received_at = Column(DateTime(timezone=True), server_default=func.now())
    keywords = Column(String)  # comma separated
    assigned_to = Column(Integer, ForeignKey("users.id"), nullable=True)

class Assignment(Base):
    __tablename__ = "assignments"
    id = Column(Integer, primary_key=True, index=True)
    message_id = Column(Integer, ForeignKey("messages.id"))
    user_id = Column(Integer, ForeignKey("users.id"))
    assigned_at = Column(DateTime(timezone=True), server_default=func.now())
    status = Column(String, default="open")

class Request(Base):
    __tablename__ = "requests"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    request_type = Column(String)  # 'leave' or 'raise'
    description = Column(Text)
    status = Column(String, default="pending")  # pending, approved, rejected
    submitted_at = Column(DateTime(timezone=True), server_default=func.now())
    reviewed_at = Column(DateTime(timezone=True), nullable=True)
    reviewed_by = Column(Integer, ForeignKey("users.id"), nullable=True)
    notes = Column(Text, nullable=True)

class Shift(Base):
    __tablename__ = "shifts"
    id = Column(Integer, primary_key=True, index=True)
    department_id = Column(Integer, ForeignKey("departments.id"))
    shift_name = Column(String)  # Morning, Afternoon, Night
    start_time = Column(String)  # HH:MM format
    end_time = Column(String)
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class ShiftAssignment(Base):
    __tablename__ = "shift_assignments"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    shift_id = Column(Integer, ForeignKey("shifts.id"))
    assigned_date = Column(String)  # YYYY-MM-DD
    created_at = Column(DateTime(timezone=True), server_default=func.now())

class TimeTracking(Base):
    __tablename__ = "time_tracking"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    check_in_time = Column(DateTime(timezone=True), nullable=True)
    check_out_time = Column(DateTime(timezone=True), nullable=True)
    date = Column(String)  # YYYY-MM-DD

class KPIMetric(Base):
    __tablename__ = "kpi_metrics"
    id = Column(Integer, primary_key=True, index=True)
    user_id = Column(Integer, ForeignKey("users.id"))
    metric_name = Column(String)  # messages_handled, response_time, satisfaction_rate
    metric_value = Column(Float)
    period = Column(String)  # YYYY-MM
    recorded_at = Column(DateTime(timezone=True), server_default=func.now())
