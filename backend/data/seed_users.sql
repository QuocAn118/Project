-- Seed data for users table
-- Password hashes are bcrypt hashes for testing purposes
-- admin@omnichat.com / admin123
-- manager@omnichat.com / manager123
-- staff@omnichat.com / staff123

INSERT INTO users (email, password_hash, full_name, phone, role, department_id, is_active) VALUES
('admin@omnichat.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYqVr/4Kfuy', 'Quản trị viên', '0901234567', 'admin', NULL, true),
('manager.sales@omnichat.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYqVr/4Kfuy', 'Nguyễn Văn A', '0902234567', 'manager', 1, true),
('manager.tech@omnichat.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYqVr/4Kfuy', 'Trần Thị B', '0903234567', 'manager', 2, true),
('manager.cs@omnichat.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYqVr/4Kfuy', 'Lê Văn C', '0904234567', 'manager', 3, true),
('staff1@omnichat.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYqVr/4Kfuy', 'Phạm Thị D', '0905234567', 'staff', 1, true),
('staff2@omnichat.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYqVr/4Kfuy', 'Hoàng Văn E', '0906234567', 'staff', 2, true),
('staff3@omnichat.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYqVr/4Kfuy', 'Vũ Thị F', '0907234567', 'staff', 3, true),
('staff4@omnichat.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYqVr/4Kfuy', 'Đỗ Văn G', '0908234567', 'staff', 1, true),
('staff5@omnichat.com', '$2b$12$LQv3c1yqBWVHxkd0LHAkCOYz6TtxMQJqhN8/LewY5GyYqVr/4Kfuy', 'Ngô Thị H', '0909234567', 'staff', 2, true);
