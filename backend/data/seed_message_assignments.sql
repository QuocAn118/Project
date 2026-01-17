-- Seed data for message_assignments table
INSERT INTO message_assignments (message_id, assigned_to, assigned_by, notes, match_score) VALUES
(1, 5, 2, 'Khách hàng muốn tìm hiểu về sản phẩm', 0.95),
(2, 6, 3, 'Lỗi kỹ thuật, cần hỗ trợ', 0.98),
(3, 7, 4, 'Khiếu nại, cần xử lý cẩn thận', 0.92),
(4, 9, 3, 'Hỏi về cài đặt, phân công cho staff kỹ thuật', 0.90),
(5, 5, 2, 'Hỏi về giao hàng', 0.85),
(6, 7, 4, 'Khiếu nại chất lượng, cần quản lý', 0.96),
(7, 8, 2, 'Khuyến mãi, có thể xử lý nhanh', 0.88),
(8, 5, 2, 'Hỏi về thanh toán, phân công', 0.87),
(9, 7, 4, 'Đổi sản phẩm, cần xử lý', 0.94),
(10, 6, 3, 'Hỏi về bảo hành', 0.89);
