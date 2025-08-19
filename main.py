import sys
from PyQt5.QtWidgets import (QApplication, QMainWindow, QAction, QToolBar,
                            QLabel, QStatusBar, QMessageBox)
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
import database

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.initUI()
        
    def initUI(self):
        self.setWindowTitle('برنامج محاسبة')
        self.setGeometry(100, 100, 1200, 800)
        self.statusBar = QStatusBar()
        self.setStatusBar(self.statusBar)
        
        # Create menu bar
        menu_bar = self.menuBar()
        
        # File menu
        file_menu = menu_bar.addMenu('الملف')
        exit_action = QAction('خروج', self)
        exit_action.triggered.connect(self.close)
        file_menu.addAction(exit_action)
        
        # Customers menu
        customers_menu = menu_bar.addMenu('العملاء')
        add_customer_action = QAction('إضافة عميل', self)
        add_customer_action.triggered.connect(lambda: self.show_status('إضافة عميل'))
        customers_menu.addAction(add_customer_action)
        
        # Suppliers menu
        suppliers_menu = menu_bar.addMenu('الموردين')
        add_supplier_action = QAction('إضافة مورد', self)
        add_supplier_action.triggered.connect(lambda: self.show_status('إضافة مورد'))
        suppliers_menu.addAction(add_supplier_action)
        
        # Products menu
        products_menu = menu_bar.addMenu('المنتجات')
        add_product_action = QAction('إضافة منتج', self)
        add_product_action.triggered.connect(lambda: self.show_status('إضافة منتج'))
        products_menu.addAction(add_product_action)
        
        # Invoices menu
        invoices_menu = menu_bar.addMenu('الفواتير')
        sales_invoice_action = QAction('فاتورة مبيعات', self)
        sales_invoice_action.triggered.connect(lambda: self.show_status('فاتورة مبيعات'))
        purchase_invoice_action = QAction('فاتورة مشتريات', self)
        purchase_invoice_action.triggered.connect(lambda: self.show_status('فاتورة مشتريات'))
        invoices_menu.addAction(sales_invoice_action)
        invoices_menu.addAction(purchase_invoice_action)
        
        # Reports menu
        reports_menu = menu_bar.addMenu('التقارير')
        sales_report_action = QAction('تقرير المبيعات', self)
        sales_report_action.triggered.connect(lambda: self.show_status('تقرير المبيعات'))
        purchase_report_action = QAction('تقرير المشتريات', self)
        purchase_report_action.triggered.connect(lambda: self.show_status('تقرير المشتريات'))
        reports_menu.addAction(sales_report_action)
        reports_menu.addAction(purchase_report_action)
        
        # Help menu
        help_menu = menu_bar.addMenu('المساعدة')
        about_action = QAction('حول البرنامج', self)
        about_action.triggered.connect(self.show_about)
        help_menu.addAction(about_action)
        
        # Create toolbar
        toolbar = QToolBar()
        self.addToolBar(toolbar)
        
        # Add actions to toolbar
        toolbar.addAction(add_customer_action)
        toolbar.addAction(add_supplier_action)
        toolbar.addAction(add_product_action)
        toolbar.addAction(sales_invoice_action)
        toolbar.addAction(purchase_invoice_action)
        
        # Main content area
        main_label = QLabel('المنطقة الرئيسية')
        self.setCentralWidget(main_label)
        
    def show_status(self, message):
        self.statusBar.showMessage(message)
        
    def show_about(self):
        QMessageBox.information(self, 'حول البرنامج', 'برنامج محاسبة - الإصدار 1.0')

if __name__ == '__main__':
    app = QApplication(sys.argv)
    main_window = MainWindow()
    main_window.show()
    sys.exit(app.exec_())