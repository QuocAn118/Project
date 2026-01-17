-- Seed data for requests table
INSERT INTO requests (user_id, type, title, description, status, reviewed_by, review_notes) VALUES
(5, 'leave', 'Xin phép nghỉ phép', 'Xin phép nghỉ 3 ngày từ 20-22/01/2026', 'pending', NULL, NULL),
(6, 'salary_increase', 'Đề nghị tăng lương', 'Đã làm việc tốt, xin tăng lương 5%', 'approved', 2, 'Đồng ý, tăng lương 5% kể từ tháng 2'),
(7, 'transfer', 'Đề nghị chuyển phòng ban', 'Muốn chuyển sang phòng kinh doanh', 'pending', NULL, NULL),
(8, 'other', 'Cải thiện môi trường làm việc', 'Đề nghị nâng cấp máy tính', 'approved', 2, 'Đã được phê duyệt, sẽ mua máy mới'),
(9, 'leave', 'Xin phép lễ', 'Xin phép lễ Tết Nguyên Đán', 'pending', NULL, NULL),
(6, 'salary_increase', 'Tăng lương thêm', 'Có thêm trách nhiệm, xin tăng lương', 'rejected', 3, 'Chưa có kế hoạch tăng lương lúc này'),
(7, 'other', 'Đề nghị khóa đào tạo', 'Muốn tham gia khóa đào tạo chuyên môn', 'approved', 4, 'Sẽ sắp xếp khóa đào tạo vào quý 2');
