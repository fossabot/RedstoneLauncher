# coding:utf-8
from PyQt5.QtWidgets import *
from qfluentwidgets import *
from qfluentwidgets import FluentIcon as FIF
from Helpers.Config import cfg
from PyQt5.QtCore import Qt

from Helpers.styleHelper import style_path


class AppilacationSettingsInterface(ScrollArea):

    def __init__(self, parent=None):
        super().__init__(parent=parent)

        self.scrollWidget = QWidget()
        self.expandLayout = ExpandLayout(self.scrollWidget)
        self.settingLabel = QLabel(self.tr("应用程序设置"), self)

        self.setObjectName("AppilacationSettingsInterface")
        self.scrollWidget.setObjectName('scrollWidget')
        self.settingLabel.setObjectName('settingLabel')

        self.InitCards()
        self.setWidget(self.scrollWidget)
        self.setWidgetResizable(True)
        self.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.setViewportMargins(0, 120, 0, 20)


        self.InitLayout()
        self.setQss()

    def InitCards(self):
        self.personalizeGroup = SettingCardGroup(self.tr("个性化"), self.scrollWidget)
        self.languageCard = ComboBoxSettingCard(
            cfg.language,
            FIF.LANGUAGE,
            self.tr('语言'),
            self.tr('设置用户界面的首选语言'),
            texts=['简体中文', '繁體中文', 'English', self.tr('使用系统设置')],
            parent=self.personalizeGroup
        )
        self.themeCard = OptionsSettingCard(
            cfg.themeMode,
            FIF.BRUSH,
            self.tr('深浅模式'),
            self.tr("更改应用程序的外观"),
            texts=[
                self.tr('浅色'), self.tr('深色'),
                self.tr('使用系统设置')
            ],
            parent=self.personalizeGroup
        )

        self.themeCard.optionChanged.connect(lambda ci: setTheme(cfg.get(ci)))


    def setSettingsQss(self):
        theme = 'dark' if isDarkTheme() else 'light'
        with open(f'resource/qss/{theme}.qss', encoding='utf-8') as f:
            self.setStyleSheet(f.read())
    def InitLayout(self):
        self.settingLabel.move(60, 63)
        self.expandLayout.setSpacing(28)
        self.expandLayout.setContentsMargins(60, 10, 60, 0)
        self.personalizeGroup.addSettingCard(self.languageCard)
        self.personalizeGroup.addSettingCard(self.themeCard)
        self.expandLayout.addWidget(self.personalizeGroup)

    def setQss(self):
        with open(style_path(), encoding='utf-8') as f:
            self.setStyleSheet(f.read())

