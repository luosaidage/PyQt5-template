from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QApplication
import sys
from ui_contral.main import CheckTool

# 直接运行即可
if __name__ == '__main__':
    if hasattr(Qt, 'AA_EnableHighDpiScaling'):
        QApplication.setAttribute(Qt.AA_EnableHighDpiScaling, True)
    if hasattr(Qt, 'AA_UseHighDpiPixmaps'):
        QApplication.setAttribute(Qt.AA_UseHighDpiPixmaps, True)

    app = QApplication(sys.argv)
    window = CheckTool()
    window.show()
    sys.exit(app.exec_())
