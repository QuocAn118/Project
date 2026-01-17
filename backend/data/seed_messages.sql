-- Seed data for messages table
INSERT INTO messages (customer_id, content, platform, direction, status) VALUES
(1, 'Tôi muốn mua sản phẩm X, giá bao nhiêu?', 'zalo', 'incoming', 'pending'),
(2, 'Sản phẩm của tôi bị lỗi, không hoạt động được', 'facebook', 'incoming', 'pending'),
(3, 'Tôi muốn được hỗ trợ về dịch vụ', 'zalo', 'incoming', 'pending'),
(4, 'Làm cách nào để cài đặt sản phẩm?', 'email', 'incoming', 'assigned'),
(5, 'Giao hàng tới đây mất bao lâu?', 'zalo', 'incoming', 'in_progress'),
(6, 'Tôi muốn khiếu nại về chất lượng sản phẩm', 'facebook', 'incoming', 'assigned'),
(7, 'Có khuyến mãi nào cho sản phẩm này không?', 'zalo', 'incoming', 'pending'),
(8, 'Làm sao để thực hiện thanh toán?', 'email', 'incoming', 'pending'),
(9, 'Tôi muốn đổi sản phẩm này', 'zalo', 'incoming', 'assigned'),
(10, 'Bảo hành kéo dài bao lâu?', 'facebook', 'incoming', 'pending');
