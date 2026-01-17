# Database Seed Data

Thư mục này chứa tất cả các file seed dữ liệu mẫu cho database OmniChat.

## Cấu trúc file

- `seed_departments.sql` - Dữ liệu mẫu cho phòng ban
- `seed_users.sql` - Dữ liệu mẫu cho người dùng (admin, manager, staff)
- `seed_customers.sql` - Dữ liệu mẫu cho khách hàng
- `seed_keywords.sql` - Dữ liệu mẫu cho từ khóa
- `seed_shifts.sql` - Dữ liệu mẫu cho ca làm việc
- `seed_kpis.sql` - Dữ liệu mẫu cho KPI
- `seed_messages.sql` - Dữ liệu mẫu cho tin nhắn
- `seed_message_assignments.sql` - Dữ liệu mẫu cho phân công tin nhắn
- `seed_requests.sql` - Dữ liệu mẫu cho yêu cầu nội bộ
- `seed_user_shifts.sql` - Dữ liệu mẫu cho phân công ca
- `seed_notifications.sql` - Dữ liệu mẫu cho thông báo
- `seed_database.py` - Script Python để chạy tất cả seed file

## Hướng dẫn sử dụng

### Cách 1: Chạy script Python (Khuyên dùng)

```bash
cd backend
python data/seed_database.py
```

### Cách 2: Chạy từng file SQL theo thứ tự

```bash
cd backend

# Chạy file seed đầu tiên
psql -U postgres -d omnichat_db -f data/seed_departments.sql

# Chạy file seed thứ hai
psql -U postgres -d omnichat_db -f data/seed_users.sql

# Cứ thế tiếp tục với các file khác...
```

### Cách 3: Dùng psql interactive mode

```bash
psql -U postgres -d omnichat_db

-- Trong psql prompt, chạy:
\i data/seed_departments.sql
\i data/seed_users.sql
-- ...
```

## Tài khoản test

### Admin
- **Email**: admin@omnichat.com
- **Password**: admin123

### Manager
- **Email**: manager.sales@omnichat.com (Phòng kinh doanh)
- **Email**: manager.tech@omnichat.com (Phòng kỹ thuật)
- **Email**: manager.cs@omnichat.com (Phòng chăm sóc khách hàng)
- **Password**: manager123

### Staff
- **Email**: staff1@omnichat.com đến staff5@omnichat.com
- **Password**: staff123

## Ghi chú

- Tất cả password đều được hash bằng bcrypt
- Các file seed được sắp xếp theo thứ tự để tôn trọng ràng buộc khóa ngoài
- Dữ liệu mẫu được tạo nhằm mục đích test và development
- Không sử dụng dữ liệu này trong production

## Clear dữ liệu

Nếu muốn xóa tất cả dữ liệu (nhưng giữ schema):

```bash
psql -U postgres -d omnichat_db

-- Trong psql prompt:
TRUNCATE TABLE notifications CASCADE;
TRUNCATE TABLE message_assignments CASCADE;
TRUNCATE TABLE messages CASCADE;
TRUNCATE TABLE requests CASCADE;
TRUNCATE TABLE user_shifts CASCADE;
TRUNCATE TABLE kpis CASCADE;
TRUNCATE TABLE keywords CASCADE;
TRUNCATE TABLE customers CASCADE;
TRUNCATE TABLE shifts CASCADE;
TRUNCATE TABLE users CASCADE;
TRUNCATE TABLE departments CASCADE;
```

Hoặc xóa hoàn toàn database:

```bash
psql -U postgres -c "DROP DATABASE IF EXISTS omnichat_db;"
psql -U postgres -c "CREATE DATABASE omnichat_db;"
psql -U postgres -d omnichat_db -f ../init_db.sql
python seed_database.py
```
