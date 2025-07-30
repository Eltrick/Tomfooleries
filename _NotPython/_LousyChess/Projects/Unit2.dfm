object Form2: TForm2
  Left = 5
  Top = 0
  Caption = 'Form2'
  ClientHeight = 496
  ClientWidth = 1042
  Color = clBtnFace
  Font.Charset = DEFAULT_CHARSET
  Font.Color = clWindowText
  Font.Height = -12
  Font.Name = 'Segoe UI'
  Font.Style = []
  Position = poDesigned
  TextHeight = 15
  object Label1: TLabel
    Left = 5
    Top = 440
    Width = 34
    Height = 15
    Caption = 'White:'
  end
  object Label2: TLabel
    Left = 5
    Top = 470
    Width = 31
    Height = 15
    Caption = 'Black:'
  end
  object Image1: TImage
    Left = 630
    Top = 8
    Width = 404
    Height = 386
  end
  object WRNGEdt: TEdit
    Left = 48
    Top = 437
    Width = 576
    Height = 23
    TabOrder = 0
  end
  object KRNGEdt: TEdit
    Left = 48
    Top = 467
    Width = 576
    Height = 23
    TabOrder = 1
  end
  object WTypeGroup: TRadioGroup
    Left = 8
    Top = 8
    Width = 185
    Height = 273
    Caption = 'White Rules'
    ItemIndex = 0
    Items.Strings = (
      'K: The King must Die'
      'L: Light Squares are Lava'
      'D: Dark Squares are Lava'
      'M: Mirror, Mirror'
      'S: Let'#39's Switch Sides')
    TabOrder = 2
  end
  object KTypeGroup: TRadioGroup
    Left = 199
    Top = 8
    Width = 194
    Height = 273
    Caption = 'Black Rules'
    ItemIndex = 0
    Items.Strings = (
      'K: The King must Die'
      'L: Light Squares are Lava'
      'D: Dark Squares are Lava'
      'M: Mirror, Mirror'
      'S: Let'#39's Switch Sides')
    TabOrder = 3
  end
  object WRNGGroup: TRadioGroup
    Left = 8
    Top = 287
    Width = 185
    Height = 144
    Caption = 'White Numbers'
    ItemIndex = 0
    Items.Strings = (
      'Seed + Serial Number'
      'Seed + Direct Key'
      'Complete Randomness')
    TabOrder = 4
  end
  object KRNGGroup: TRadioGroup
    Left = 199
    Top = 287
    Width = 194
    Height = 144
    Caption = 'Black Numbers'
    ItemIndex = 0
    Items.Strings = (
      'Seed + Serial Number'
      'Seed + Direct Key'
      'Complete Randomness')
    TabOrder = 5
  end
  object Panel1: TPanel
    Left = 630
    Top = 398
    Width = 404
    Height = 92
    TabOrder = 6
    object StepLbl: TLabel
      Left = 8
      Top = 37
      Width = 25
      Height = 15
      Caption = 'Fuck'
    end
    object CalcBtn: TButton
      Left = 8
      Top = 8
      Width = 185
      Height = 25
      Caption = 'Calculate'
      TabOrder = 0
      OnClick = CalcBtnClick
    end
    object SizeBtn: TButton
      Left = 199
      Top = 10
      Width = 194
      Height = 25
      Caption = 'Change Size'
      TabOrder = 1
      OnClick = SizeBtnClick
    end
    object PrevBtn: TButton
      Left = 8
      Top = 55
      Width = 185
      Height = 29
      Caption = 'Previous Move'
      TabOrder = 2
      OnClick = PrevBtnClick
    end
    object NextBtn: TButton
      Left = 199
      Top = 55
      Width = 194
      Height = 29
      Caption = 'Next Move'
      TabOrder = 3
      OnClick = NextBtnClick
    end
  end
  object Memo1: TMemo
    Left = 399
    Top = 8
    Width = 225
    Height = 423
    Font.Charset = ANSI_CHARSET
    Font.Color = clWindowText
    Font.Height = -15
    Font.Name = 'Consolas'
    Font.Style = [fsBold]
    ParentFont = False
    TabOrder = 7
  end
end
