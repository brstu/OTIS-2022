object Form1: TForm1
  Left = 264
  Top = 308
  BorderIcons = [biSystemMenu, biMinimize]
  BorderStyle = bsSingle
  Caption = #1058#1086#1087#1086#1083#1086#1075#1080#1095#1077#1089#1082#1072#1103' '#1089#1086#1088#1090#1080#1088#1086#1074#1082#1072
  ClientHeight = 608
  ClientWidth = 862
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -11
  Font.Name = 'MS Sans Serif'
  Font.Style = []
  OldCreateOrder = False
  Position = poScreenCenter
  OnCreate = FormCreate
  PixelsPerInch = 96
  TextHeight = 13
  object Label1: TLabel
    Left = 536
    Top = 8
    Width = 107
    Height = 13
    Caption = #1052#1072#1090#1088#1080#1094#1072' '#1080#1085#1094#1077#1076#1077#1085#1094#1080#1081
  end
  object TabControl1: TTabControl
    Left = 0
    Top = 0
    Width = 528
    Height = 608
    TabOrder = 0
    Tabs.Strings = (
      #1043#1088#1072#1092
      #1054#1090#1089#1086#1088#1090#1080#1088#1086#1074#1072#1085#1099#1081' '#1075#1088#1072#1092)
    TabIndex = 0
    OnChange = TabControl1Change
    OnChanging = TabControl1Changing
    object PB: TPaintBox
      Left = 4
      Top = 24
      Width = 520
      Height = 580
      Cursor = crArrow
      Align = alClient
      OnMouseDown = PBMouseDown
      OnMouseMove = PBMouseMove
      OnMouseUp = PBMouseUp
      OnPaint = PBPaint
    end
  end
  object Grid: TStringGrid
    Left = 528
    Top = 24
    Width = 329
    Height = 321
    ColCount = 2
    DefaultColWidth = 15
    DefaultRowHeight = 15
    RowCount = 2
    Options = [goFixedVertLine, goFixedHorzLine, goVertLine, goHorzLine, goThumbTracking]
    TabOrder = 1
  end
  object Button1: TButton
    Left = 536
    Top = 424
    Width = 121
    Height = 25
    Caption = #1057#1086#1088#1090#1080#1088#1086#1074#1072#1090#1100' '#1075#1088#1072#1092
    TabOrder = 2
    OnClick = Button1Click
  end
  object GroupBox1: TGroupBox
    Left = 536
    Top = 472
    Width = 129
    Height = 129
    Caption = #1056#1080#1089#1086#1074#1072#1085#1080#1077' '#1075#1088#1072#1092#1072
    TabOrder = 3
    object btnVertex: TSpeedButton
      Left = 8
      Top = 16
      Width = 105
      Height = 33
      AllowAllUp = True
      GroupIndex = 1
      Caption = #1059#1089#1090#1072#1085#1086#1074#1082#1072' '#1074#1077#1088#1096#1080#1085
    end
    object btnLinks: TSpeedButton
      Left = 8
      Top = 48
      Width = 105
      Height = 33
      AllowAllUp = True
      GroupIndex = 1
      Caption = #1059#1089#1090#1072#1085#1086#1082#1072' '#1089#1074#1103#1079#1077#1081
    end
    object btnMove: TSpeedButton
      Left = 8
      Top = 80
      Width = 105
      Height = 33
      AllowAllUp = True
      GroupIndex = 1
      Caption = #1055#1077#1088#1077#1084#1077#1097#1077#1085#1080#1077
    end
  end
  object Button2: TButton
    Left = 688
    Top = 424
    Width = 153
    Height = 25
    Caption = #1053#1077#1086#1088#1080#1077#1085#1090#1080#1088#1086#1074#1072#1085#1085#1099#1081' '#1075#1088#1072#1092
    TabOrder = 4
    OnClick = Button2Click
  end
end
