-- Seed data for notifications table
INSERT INTO notifications (user_id, title, message, type, is_read, link) VALUES
(1, 'Báo cáo hệ thống', 'Hệ thống đã khôi phục xong sau bảo trì', 'info', true, '/admin/system'),
(2, 'Công việc mới', 'Bạn có 5 tin nhắn chưa xử lý', 'warning', false, '/manager/messages'),
(3, 'Công việc mới', 'Bạn có 3 tin nhắn chưa xử lý', 'warning', false, '/manager/messages'),
(4, 'Công việc mới', 'Bạn có 2 tin nhắn chưa xử lý', 'warning', false, '/manager/messages'),
(5, 'Tin nhắn mới', 'Bạn có tin nhắn mới từ khách hàng', 'info', false, '/staff/messages'),
(6, 'Tin nhắn mới', 'Bạn có tin nhắn mới từ khách hàng', 'info', false, '/staff/messages'),
(7, 'Tin nhắn mới', 'Bạn có tin nhắn mới từ khách hàng', 'info', true, '/staff/messages'),
(8, 'Xin lỗi, có sự cố', 'Bạn đã bỏ lỡ tin nhắn từ khách hàng quan trọng', 'error', false, '/staff/messages'),
(1, 'Cập nhật hệ thống', 'Phiên bản mới sẽ được phát hành vào tuần tới', 'info', false, '/admin/system'),
(9, 'Thành tích tốt', 'Bạn đã đạt KPI của tháng này', 'success', true, '/staff/kpi');
