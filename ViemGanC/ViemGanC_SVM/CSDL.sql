USE [ViemGanC]
GO
/****** Object:  Table [dbo].[SucKhoe]    Script Date: 28/05/2023 10:24:12 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[SucKhoe](
	[TenDangNhap] [varchar](255) NULL,
	[Ngay] [date] NULL,
	[Tuoi] [int] NULL,
	[Sex] [int] NULL,
	[ALB] [float] NULL,
	[ALP] [float] NULL,
	[ALT] [float] NULL,
	[AST] [float] NULL,
	[BIL] [float] NULL,
	[CHE] [float] NULL,
	[CHOL] [float] NULL,
	[CREA] [float] NULL,
	[GGT] [float] NULL,
	[PROT] [float] NULL,
	[KetQuaDuDoan] [nvarchar](255) NULL
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
/****** Object:  Table [dbo].[TaiKhoan]    Script Date: 28/05/2023 10:24:12 ******/
SET ANSI_NULLS ON
GO
SET QUOTED_IDENTIFIER ON
GO
SET ANSI_PADDING ON
GO
CREATE TABLE [dbo].[TaiKhoan](
	[TenDangNhap] [varchar](255) NOT NULL,
	[MatKhau] [varchar](255) NULL,
	[SoDienThoai] [varchar](20) NULL,
PRIMARY KEY CLUSTERED 
(
	[TenDangNhap] ASC
)WITH (PAD_INDEX = OFF, STATISTICS_NORECOMPUTE = OFF, IGNORE_DUP_KEY = OFF, ALLOW_ROW_LOCKS = ON, ALLOW_PAGE_LOCKS = ON) ON [PRIMARY]
) ON [PRIMARY]

GO
SET ANSI_PADDING OFF
GO
INSERT [dbo].[SucKhoe] ([TenDangNhap], [Ngay], [Tuoi], [Sex], [ALB], [ALP], [ALT], [AST], [BIL], [CHE], [CHOL], [CREA], [GGT], [PROT], [KetQuaDuDoan]) VALUES (N'Giang', CAST(N'2023-05-27' AS Date), 30, 0, 4.2, 70, 15, 20, 0.7, 5.2, 180, 0.8, 10, 7.5, N'Không bị viêm gan C')
INSERT [dbo].[SucKhoe] ([TenDangNhap], [Ngay], [Tuoi], [Sex], [ALB], [ALP], [ALT], [AST], [BIL], [CHE], [CHOL], [CREA], [GGT], [PROT], [KetQuaDuDoan]) VALUES (N'Giang', CAST(N'2023-05-28' AS Date), 40, 0, 3.8, 85, 60, 70, 1.2, 6.8, 200, 1.2, 45, 6.8, N'Không bị viêm gan C')
INSERT [dbo].[TaiKhoan] ([TenDangNhap], [MatKhau], [SoDienThoai]) VALUES (N'Admin', N'123', N'0123456789')
INSERT [dbo].[TaiKhoan] ([TenDangNhap], [MatKhau], [SoDienThoai]) VALUES (N'Giang', N'123', N'0151155154')
INSERT [dbo].[TaiKhoan] ([TenDangNhap], [MatKhau], [SoDienThoai]) VALUES (N'Teo', N'123', N'01215465658')
ALTER TABLE [dbo].[SucKhoe]  WITH CHECK ADD FOREIGN KEY([TenDangNhap])
REFERENCES [dbo].[TaiKhoan] ([TenDangNhap])
GO
