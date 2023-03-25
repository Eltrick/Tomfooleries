unit Unit1;

//Lousy Chess - solver
//made by MageMage81

interface

uses
  Winapi.Windows, Winapi.Messages, System.SysUtils, System.Variants, System.Classes, Vcl.Graphics,
  Vcl.Controls, Vcl.Forms, Vcl.Dialogs, Vcl.StdCtrls, Vcl.ExtCtrls, pngimage;

type
  TForm1 = class(TForm)
    Image1: TImage;
    Memo1: TMemo;
    Panel1: TPanel;
    PrevBtn: TButton;
    NextBtn: TButton;
    StepLbl: TLabel;
    KTypeGroup: TRadioGroup;
    WTypeGroup: TRadioGroup;
    WRNGGroup: TRadioGroup;
    KRNGGroup: TRadioGroup;
    WRNGEdt: TEdit;
    KRNGEdt: TEdit;
    Label2: TLabel;
    Label3: TLabel;
    CalcBtn: TButton;
    SizeBtn: TButton;
    procedure FormCreate(Sender: TObject);
    procedure ResetSmall();
    procedure ResetBig();
    procedure SizeBtnClick(Sender: TObject);
    procedure CalcBtnClick(Sender: TObject);
    procedure AppendPart(Text:String);
    function MakeMove(moveS : String; leave : Integer; NewElement: Boolean) : String;
    function AnyMove(Reverse: Boolean; Number :Integer; White: Boolean):String;
    procedure DrawMove(moveS : String; leave : Integer);
    procedure PrevBtnClick(Sender: TObject);
    procedure NextBtnClick(Sender: TObject);
    function KingKilling(Reverse: Boolean; Number :Integer; White: Boolean):String;
    function LightLava(Reverse: Boolean; Number :Integer; White: Boolean):String;
    function DarkLava(Reverse: Boolean; Number :Integer; White: Boolean):String;
    function KingDead(Reverse: Boolean; Number :Integer; White: Boolean):String;
    function Mirror(Reverse: Boolean; Number :Integer; White: Boolean):String;
    function Switch(Reverse: Boolean; Number :Integer; White: Boolean):String;
  private
    { Private declarations }
  public
    { Public declarations }
  end;

//♚  ♛  ♝  ♞  ♜  ♟︎ ♙ ♖ ♘ ♗ ♕ ♔     384 x 384 ->  48 x 48 or   64 x 64
//-6  -5  -3  -2  -4  -1  1  4  2  3  5  6  0

var
  Form1: TForm1;
  Big, KingAlive: Boolean;
  Pos: Array of Array of Integer;
  possibleMoves : Array of String;
  moveList: Array of String;  //P1 X1 Y1 X2 Y2 P2 -> +PXYXYP P1 is w/ +/i; P2 is w/o
  wx, wy, kx, ky, moveAt, hgt, wdt: Integer;

const
  clBright = '$FFFFFF';
  clDark = '$996666';

implementation

{$R *.dfm}

procedure TForm1.ResetSmall();
var
  i, j : Integer;
  Picture: TPicture;
begin
  wdt := 5;
  hgt := 6;
  SetLength(Pos, 5);
  for i := 0 to 4 do
    SetLength(Pos[i], 6);

  with Image1.Canvas do
    begin
      Brush.Color := StringToColor(clBright);
      Pen.Color := StringToColor('$000000');   //StringToColor('$0000FF') - $BBGGRR
      Rectangle(0, 0, 384, 384);
      Rectangle(32, 0, 352, 384);
      Brush.Color :=  StringToColor(clDark);
      for i := 0 to 4 do
        for j := 0 to 5 do
          begin
            if (i+j) mod 2 = 1 then
              Rectangle(32+64*i, 64*j, 96+64*i, 64+64*j);
          end;
      Font.Size := 48;
      Brush.Color := StringToColor('$FFFFFF');

    end;

  Pos[0,0] := -6; //Black King
  kx := 0;
  ky := 0;
  Pos[1,0] := -5; //Black Queen
  Pos[2,0] := -3; //Black Bishop
  Pos[3,0] := -2; //Black Knight
  Pos[4,0] := -4; //Black Rook
  Pos[4,5] := 6;  //White King
  wx := 4;
  wy := 5;
  Pos[3,5] := 5;  //White Queen
  Pos[2,5] := 3;  //White Bishop
  Pos[1,5] := 2;  //White Knight
  Pos[0,5] := 4;  //White Rook
  for i := 0 to 4 do
    begin
      Pos[i,1] := -1; //Black Pawns
      Pos[i,4] := 1;  //White Pawns
      Pos[i,2] := 0;  //Empty
      Pos[i,3] := 0;
    end;

  for i := 0 to 4 do
    for j := 0 to 5 do
      begin
        Picture := TPicture.Create;
        case Pos[i,j] of     //♚  ♛  ♝  ♞  ♜  ♟︎ ♙ ♖ ♘ ♗ ♕ ♔
        1: Picture.LoadFromFile('..\Pictures\WP.png');
        2: Picture.LoadFromFile('..\Pictures\WN.png');
        3: Picture.LoadFromFile('..\Pictures\WB.png');
        4: Picture.LoadFromFile('..\Pictures\WR.png');
        5: Picture.LoadFromFile('..\Pictures\WQ.png');
        6: Picture.LoadFromFile('..\Pictures\WK.png');
        -1: Picture.LoadFromFile('..\Pictures\KP.png');
        -2: Picture.LoadFromFile('..\Pictures\KN.png');
        -3: Picture.LoadFromFile('..\Pictures\KB.png');
        -4: Picture.LoadFromFile('..\Pictures\KR.png');
        -5: Picture.LoadFromFile('..\Pictures\KQ.png');
        -6: Picture.LoadFromFile('..\Pictures\KK.png');
        end;
        if Pos[i,j] <> 0 then
          begin
            //Image1.Canvas.TextOut(40+64*i, 8+64*j, Symbol);
            Image1.Canvas.Draw(40+64*i,8+64*j,Picture.Graphic);
          end;
      end;
  Picture.Free;
end;

procedure TForm1.SizeBtnClick(Sender: TObject);
begin
  Big := Not(Big);
  if Big then
    ResetBig()
  else
    ResetSmall();
  PrevBtn.Enabled := False;
  NextBtn.Enabled := False;
end;

procedure TForm1.ResetBig();
var
  i, j : Integer;
  Picture: TPicture;
begin
  hgt := 8;
  wdt := 8;
  SetLength(Pos, 8);
  for i := 0 to 7 do
    SetLength(Pos[i], 8);

  with Image1.Canvas do
    begin
      Brush.Color := StringToColor(clBright);
      Pen.Color := StringToColor('$000000');   //StringToColor('$0000FF') - $BBGGRR
      Rectangle(0, 0, 384, 384);
      Brush.Color :=  StringToColor(clDark);
      for i := 0 to 7 do
        for j := 0 to 7 do
          begin
            if (i+j) mod 2 = 1 then
              Rectangle(48*i, 48*j, 48+48*i, 48+48*j);
          end;
      Font.Size := 48;
      Brush.Color := StringToColor('$FFFFFF');

    end;

  Pos[4,0] := -6; //Black King
  kx := 4;
  ky := 0;
  Pos[3,0] := -5; //Black Queen
  Pos[2,0] := -3; //Black Bishop
  Pos[5,0] := -3;
  Pos[1,0] := -2; //Black Knight
  Pos[6,0] := -2;
  Pos[0,0] := -4; //Black Rook
  Pos[7,0] := -4;
  Pos[4,7] := 6;  //White King
  wx := 4;
  wy := 7;
  Pos[3,7] := 5;  //White Queen
  Pos[2,7] := 3;  //White Bishop
  Pos[5,7] := 3;
  Pos[1,7] := 2;  //White Knight
  Pos[6,7] := 2;
  Pos[0,7] := 4;  //White Rook
  Pos[7,7] := 4;
  for i := 0 to 7 do
    begin
      Pos[i,1] := -1; //Black Pawns
      Pos[i,6] := 1;  //White Pawns
      Pos[i,2] := 0;  //Empty
      Pos[i,3] := 0;
      Pos[i,4] := 0;
      Pos[i,5] := 0;
    end;

  for i := 0 to 7 do
    for j := 0 to 7 do
      begin
        Picture := TPicture.Create;
        case Pos[i,j] of     //♚  ♛  ♝  ♞  ♜  ♟︎ ♙ ♖ ♘ ♗ ♕ ♔
        1: Picture.LoadFromFile('..\Pictures\WP.png');
        2: Picture.LoadFromFile('..\Pictures\WN.png');
        3: Picture.LoadFromFile('..\Pictures\WB.png');
        4: Picture.LoadFromFile('..\Pictures\WR.png');
        5: Picture.LoadFromFile('..\Pictures\WQ.png');
        6: Picture.LoadFromFile('..\Pictures\WK.png');
        -1: Picture.LoadFromFile('..\Pictures\KP.png');
        -2: Picture.LoadFromFile('..\Pictures\KN.png');
        -3: Picture.LoadFromFile('..\Pictures\KB.png');
        -4: Picture.LoadFromFile('..\Pictures\KR.png');
        -5: Picture.LoadFromFile('..\Pictures\KQ.png');
        -6: Picture.LoadFromFile('..\Pictures\KK.png');
        end;
        if Pos[i,j] <> 0 then
          begin
            Image1.Canvas.Draw(48*i,48*j,Picture.Graphic);
          end;
      end;
  Picture.Free;
end;

procedure TForm1.FormCreate(Sender: TObject);
begin
  Big := False;
  moveAt := 0;
  ResetSmall();
end;


function Base(SB:String) :String;
var
  i, Ordinal, next, Len: Integer;
  Line, newLine, fin : String;
begin
  if Length(SB) = 41 then
    result := SB
  else
  begin
    Line := Copy(SB, 2, Length(SB)-1);
    newLine := '';
    for i := 1 to Length(Line) do
    begin
      Ordinal := Ord(Line[i]);
      if (Ordinal > 64) and (Ordinal < 123) then
      begin
        if Ordinal < 91 then
          Ordinal := Ordinal + 32;
        Ordinal := Ordinal - 96;
        newLine := newline + IntToStr(Ordinal);
      end
      else
        newLine := newLine + Line[i];
    end;
    fin := SB[1];
    while Length(fin) < 41 do
    begin
      Len := Length(fin);
      next := StrToInt(fin[Len]) + StrToInt(newLine[((Len-1) mod Length(newLine))+1]);
      fin := fin + IntToStr(next mod 10);
    end;
    Base := fin;
  end;
end;

function Key(Start:String) :String;
var
  Len : Integer;
begin
  Len := Length(Start) - 1;
  while Length(Start) < 41 do
  begin
    Start := Start + Copy(Start, 2, Len);
  end;
  Key := Copy(Start, 1, 41);
end;

function RNG(Fest:String) :String;
var
  part :String;
begin
  if Length(Fest) <= 41 then
    part := Fest
  else
    part := Copy(Fest, 1, 41);
  while Length(part)<41 do
  begin
    part := part + IntToStr(Random(10));
  end;
  RNG := part;
end;

//##############################################################################
function GetPawn(White: Boolean; x, y :Integer): TArray<String>;
var
  help : TArray<String>;
begin
  SetLength(help, 0);
  if White then
  begin
    if (x > 0) then
      if (Pos[x-1][y-1] <0) then
      begin
        SetLength(help, Length(help)+1);
        help[Length(help)-1] := '+1' + IntToStr(x) + IntToStr(y) + IntToStr(x-1) + IntToStr(y-1)
      end;

    if (Pos[x][y-1] = 0) then
    begin
      SetLength(help, Length(help)+1);
      help[Length(help)-1] := '+1' + IntToStr(x) + IntToStr(y) + IntToStr(x) + IntToStr(y-1)
    end;

    if (x < wdt-1) then
      if (Pos[x+1][y-1] <0) then
      begin
        SetLength(help, Length(help)+1);
        help[Length(help)-1] := '+1' + IntToStr(x) + IntToStr(y) + IntToStr(x+1) + IntToStr(y-1)
      end;
  end
  else
  begin
    if (x > 0) then
      if (Pos[x-1][y+1] > 0) then
      begin
        SetLength(help, Length(help)+1);
        help[Length(help)-1] := '-1' + IntToStr(x) + IntToStr(y) + IntToStr(x-1) + IntToStr(y+1)
      end;

    if (Pos[x][y+1] = 0) then
    begin
      SetLength(help, Length(help)+1);
      help[Length(help)-1] := '-1' + IntToStr(x) + IntToStr(y) + IntToStr(x) + IntToStr(y+1)
    end;

    if (x < wdt-1) then
      if (Pos[x+1][y+1] > 0) then
      begin
        SetLength(help, Length(help)+1);
        help[Length(help)-1] := '-1' + IntToStr(x) + IntToStr(y) + IntToStr(x+1) + IntToStr(y+1)
      end;
  end;
  result := help;
end;

//##############################################################################
function GetKnight(multiplier, x, y :Integer): TArray<String>;
var
  base: String;
  bottom, right : Integer;
  help : TArray<String>;
begin
  if multiplier > 0 then
    base := '+2' + IntToStr(x) + IntToStr(y)
  else
    base := '-2' + IntToStr(x) + IntToStr(y);

  bottom := hgt - y - 1;
  right := wdt - x - 1;
  SetLength(help, 0);

  if x > 0 then    //one field to left border
  begin
    if x > 1 then  //two field to left border
    begin
      if bottom > 0 then //one field to bottom
        if Pos[x-2][y+1] * multiplier <= 0 then // 2 left, 1 down
        begin
          SetLength(help, Length(help)+1);
          help[Length(help)-1] := base + IntToStr(x-2) + IntToStr(y+1)
        end;
      if y > 0 then     //one field to top
        if Pos[x-2][y-1] * multiplier <= 0 then // 2 left, 1 up
        begin
          SetLength(help, Length(help)+1);
          help[Length(help)-1] := base + IntToStr(x-2) + IntToStr(y-1)
        end;
    end;
    if bottom > 1 then //two field to bottom
      if Pos[x-1][y+2] * multiplier <= 0 then // 1 left, 2 down
      begin
        SetLength(help, Length(help)+1);
        help[Length(help)-1] := base + IntToStr(x-1) + IntToStr(y+2)
      end;
    if y > 1 then      //two field to top
      if Pos[x-1][y-2] * multiplier <= 0 then // 1 left, 2 up
      begin
        SetLength(help, Length(help)+1);
        help[Length(help)-1] := base + IntToStr(x-1) + IntToStr(y-2)
      end;
  end;

  if right > 0 then    //one field to right border
  begin
    if bottom > 1 then //two field to bottom
      if Pos[x+1][y+2] * multiplier <= 0 then // 1 right, 2 down
      begin
        SetLength(help, Length(help)+1);
        help[Length(help)-1] := base + IntToStr(x+1) + IntToStr(y+2)
      end;
    if y > 1 then      //two field to top
      if Pos[x+1][y-2] * multiplier <= 0 then // 1 right, 2 up
      begin
        SetLength(help, Length(help)+1);
        help[Length(help)-1] := base + IntToStr(x+1) + IntToStr(y-2)
      end;

    if right > 1 then  //two field to right border
    begin
      if bottom > 0 then //one field to bottom
        if Pos[x+2][y+1] * multiplier <= 0 then // 2 right, 1 down
        begin
          SetLength(help, Length(help)+1);
          help[Length(help)-1] := base + IntToStr(x+2) + IntToStr(y+1)
        end;
      if y > 0 then     //one field to top
        if Pos[x+2][y-1] * multiplier <= 0 then // 2 right, 1 up
        begin
          SetLength(help, Length(help)+1);
          help[Length(help)-1] := base + IntToStr(x+2) + IntToStr(y-1)
        end;
    end;
  end;
  result := help;
end;

//##############################################################################
function GetBishop(multiplier, x, y :Integer): TArray<String>;
var
  base: String;
  bottom, right, i : Integer;
  help, part : TArray<String>;
  contDown, contUp : Boolean;
begin
  if multiplier > 0 then
    base := '+3' + IntToStr(x) + IntToStr(y)
  else
    base := '-3' + IntToStr(x) + IntToStr(y);

  bottom := hgt - y - 1;
  right := wdt - x - 1;

  SetLength(part, 0);
  if bottom > 0 then
    if Pos[x][y+1] = 0 then
    begin
      SetLength(part, Length(part)+1);
      part[Length(part)-1] := base + IntToStr(x) + IntToStr(y+1);
    end;

  contDown := True;
  contUp := True;

  i := 1;
  while contDown or contUp do       //part counter order
  begin
    if ContUp then   //going to top left
    begin
      if (x >= i) and (y >= i) then
        if Pos[x-i][y-i] * multiplier <= 0 then
        begin
          if Not (Pos[x-i][y-i] = 0) then
            ContUp := False;
          SetLength(part, Length(part)+1);
          part[Length(part)-1] := base + IntToStr(x-i) + IntToStr(y-i);
        end
        else
          ContUp := False
      else
        ContUp := False;
    end;

    if (x > 0) and (i = 1) then
      if Pos[x-1][y] = 0 then
      begin
        SetLength(part, Length(part)+1);
        part[Length(part)-1] := base + IntToStr(x-1) + IntToStr(y);
      end;

    if ContDown then  //going to bottom left
    begin
      if (x >= i) and (bottom >= i) then
        if Pos[x-i][y+i] * multiplier <= 0 then
        begin
          if Not (Pos[x-i][y+i] = 0) then
            ContDown := False;
          SetLength(part, Length(part)+1);
          part[Length(part)-1] := base + IntToStr(x-i) + IntToStr(y+i);
        end
        else
          ContDown := False
      else
        ContDown := False;
    end;
    i := i + 1;
  end;

  SetLength(help, Length(part));
  for i := 0 to Length(part)-1 do
    help[i] := part[Length(part)-i-1];

  if y > 0 then
    if Pos[x][y-1] = 0 then
    begin
      SetLength(help, Length(help)+1);
      help[Length(help)-1] := base + IntToStr(x) + IntToStr(y-1);
    end;

  contDown := True;
  contUp := True;
  i := 1;
  while contDown or contUp do     //part in order
  begin
    if ContDown then  //going to bottom right
    begin
      if (right >= i) and (bottom >= i) then
        if Pos[x+i][y+i] * multiplier <= 0 then
        begin
          if Not (Pos[x+i][y+i] = 0) then
            ContDown := False;
          SetLength(help, Length(help)+1);
          help[Length(help)-1] := base + IntToStr(x+i) + IntToStr(y+i);
        end
        else
          ContDown := False
      else
        ContDown := False;
    end;

    if (right > 0) and (i = 1) then
      if Pos[x+1][y] = 0 then
      begin
        SetLength(help, Length(help)+1);
        help[Length(help)-1] := base + IntToStr(x+1) + IntToStr(y);
      end;

    if ContUp then   //going to top right
    begin
      if (right >= i) and (y >= i) then
        if Pos[x+i][y-i] * multiplier <= 0 then
        begin
          if Not (Pos[x+i][y-i] = 0) then
            ContUp := False;
          SetLength(help, Length(help)+1);
          help[Length(help)-1] := base + IntToStr(x+i) + IntToStr(y-i);
        end
        else
          ContUp := False
      else
        ContUp := False;
    end;

    i := i + 1;
  end;

  result := help;
end;

//##############################################################################
function GetRook(multiplier, x, y :Integer): TArray<String>;
var
  base: String;
  bottom, right, i : Integer;
  help, part : TArray<String>;
  cont : Boolean;
begin
  if multiplier > 0 then
    base := '+4' + IntToStr(x) + IntToStr(y)
  else
    base := '-4' + IntToStr(x) + IntToStr(y);

  bottom := hgt - y - 1;
  right := wdt - x - 1;

  SetLength(part, 0);
  cont := True;
  i := 1;
  while cont do    //going down
  begin
    if bottom >= i then
      if Pos[x][y+i] * multiplier <= 0 then
      begin
        if Not(Pos[x][y+i] = 0) then
          cont := False;
        SetLength(part, Length(part)+1);
        part[Length(part)-1] := base + IntToStr(x) + IntToStr(y+i);
      end
      else
        cont := False
    else
      cont := False;
    i := i + 1;
  end;

  cont := True;
  i := 1;
  while cont do     // going left
  begin
    if x >= i then
      if Pos[x-i][y] * multiplier <= 0 then
      begin
        if Not(Pos[x-i][y] = 0) then
          cont := False;
        SetLength(part, Length(part)+1);
        part[Length(part)-1] := base + IntToStr(x-i) + IntToStr(y);
      end
      else
        cont := False
    else
      cont := False;
    i := i + 1;
  end;

  SetLength(help, Length(part));
  for i := 0 to Length(part)-1 do
    help[i] := part[Length(part)-i-1];

  cont := True;
  i := 1;
  while cont do    //going up
  begin
    if y >= i then
      if Pos[x][y-i] * multiplier <= 0 then
      begin
        if Not(Pos[x][y-i] = 0) then
          cont := False;
        SetLength(help, Length(help)+1);
        help[Length(help)-1] := base + IntToStr(x) + IntToStr(y-i);
      end
      else
        cont := False
    else
      cont := False;
    i := i + 1;
  end;

  cont := True;
  i := 1;
  while cont do     // going right
  begin
    if right >= i then
      if Pos[x+i][y] * multiplier <= 0 then
      begin
        if Not(Pos[x+i][y] = 0) then
          cont := False;
        SetLength(help, Length(help)+1);
        help[Length(help)-1] := base + IntToStr(x+i) + IntToStr(y);
      end
      else
        cont := False
    else
      cont := False;
    i := i + 1;
  end;

  result := help;
end;

//##############################################################################
function GetQueen(multiplier, x, y :Integer): TArray<String>;
var
  base: String;
  bottom, right, i : Integer;
  help, part : TArray<String>;
  contDown, contUp, cont : Boolean;
begin
  if multiplier > 0 then
    base := '+5' + IntToStr(x) + IntToStr(y)
  else
    base := '-5' + IntToStr(x) + IntToStr(y);

  bottom := hgt - y - 1;
  right := wdt - x - 1;

  SetLength(part, 0);
  cont := True;
  i := 1;
  while cont do    //going down
  begin
    if bottom >= i then
      if Pos[x][y+i] * multiplier <= 0 then
      begin
        if Not(Pos[x][y+i] = 0) then
          cont := False;
        SetLength(part, Length(part)+1);
        part[Length(part)-1] := base + IntToStr(x) + IntToStr(y+i);
      end
      else
        cont := False
    else
      cont := False;
    i := i + 1;
  end;

  cont := True;
  contDown := True;
  contUp := True;
  i := 1;
  while (contDown or contUp) or cont do
  begin
    if ContUp then   //going to top left
    begin
      if (x >= i) and (y >= i) then
        if Pos[x-i][y-i] * multiplier <= 0 then
        begin
          if Not (Pos[x-i][y-i] = 0) then
            ContUp := False;
          SetLength(part, Length(part)+1);
          part[Length(part)-1] := base + IntToStr(x-i) + IntToStr(y-i);
        end
        else
          ContUp := False
      else
        ContUp := False;
    end;

    if cont then     //going straight left
    begin
      if x >= i then
        if Pos[x-i][y] * multiplier <= 0 then
        begin
          if Not(Pos[x-i][y] = 0) then
            cont := False;
          SetLength(part, Length(part)+1);
          part[Length(part)-1] := base + IntToStr(x-i) + IntToStr(y);
        end
        else
          cont := False
      else
        cont := False;
    end;

    if ContDown then  //going to bottom left
    begin
      if (x >= i) and (bottom >= i) then
        if Pos[x-i][y+i] * multiplier <= 0 then
        begin
          if Not (Pos[x-i][y+i] = 0) then
            ContDown := False;
          SetLength(part, Length(part)+1);
          part[Length(part)-1] := base + IntToStr(x-i) + IntToStr(y+i);
        end
        else
          ContDown := False
      else
        ContDown := False;
    end;
    i := i + 1;
  end;

  SetLength(help, Length(part));
  for i := 0 to Length(part)-1 do
    help[i] := part[Length(part)-i-1];


  cont := True;
  i := 1;
  while cont do    //going up
  begin
    if y >= i then
      if Pos[x][y-i] * multiplier <= 0 then
      begin
        if Not(Pos[x][y-i] = 0) then
          cont := False;
        SetLength(help, Length(help)+1);
        help[Length(help)-1] := base + IntToStr(x) + IntToStr(y-i);
      end
      else
        cont := False
    else
      cont := False;
    i := i + 1;
  end;

  cont := True;
  contDown := True;
  contUp := True;
  i := 1;
  while (contDown or contUp) or cont do
  begin
  if ContDown then  //going to bottom right
    begin
      if (right >= i) and (bottom >= i) then
        if Pos[x+i][y+i] * multiplier <= 0 then
        begin
          if Not (Pos[x+i][y+i] = 0) then
            ContDown := False;
          SetLength(help, Length(help)+1);
          help[Length(help)-1] := base + IntToStr(x+i) + IntToStr(y+i);
        end
        else
          ContDown := False
      else
        ContDown := False;
    end;

    if cont then     //going straight right
    begin
      if right >= i then
        if Pos[x+i][y] * multiplier <= 0 then
        begin
          if Not(Pos[x+i][y] = 0) then
            cont := False;
          SetLength(help, Length(help)+1);
          help[Length(help)-1] := base + IntToStr(x+i) + IntToStr(y);
        end
        else
          cont := False
      else
        cont := False;
    end;

    if ContUp then   //going to top right
    begin
      if (right >= i) and (y >= i) then
        if Pos[x+i][y-i] * multiplier <= 0 then
        begin
          if Not (Pos[x+i][y-i] = 0) then
            ContUp := False;
          SetLength(help, Length(help)+1);
          help[Length(help)-1] := base + IntToStr(x+i) + IntToStr(y-i);
        end
        else
          ContUp := False
      else
        ContUp := False;
    end;

    i := i + 1;
  end;

  result := help;
end;

//##############################################################################
function GetKing(multiplier, x, y :Integer): TArray<String>;
var
  base: String;
  bottom, right : Integer;
  help : TArray<String>;
begin
  if multiplier > 0 then
    base := '+6' + IntToStr(x) + IntToStr(y)
  else
    base := '-6' + IntToStr(x) + IntToStr(y);

  bottom := hgt - y - 1;
  right := wdt - x - 1;
  SetLength(help, 0);
  if x > 0 then
  begin
    if bottom > 0 then
      if Pos[x-1][y+1] * multiplier <= 0 then //bl
      begin
        SetLength(help, Length(help)+1);
        help[Length(help)-1] := base + IntToStr(x-1) + IntToStr(y+1);
      end;

    if Pos[x-1][y] * multiplier <= 0 then //cl
    begin
      SetLength(help, Length(help)+1);
      help[Length(help)-1] := base + IntToStr(x-1) + IntToStr(y);
    end;

    if y > 0 then
      if Pos[x-1][y-1] * multiplier <= 0 then //tl
      begin
        SetLength(help, Length(help)+1);
        help[Length(help)-1] := base + IntToStr(x-1) + IntToStr(y-1);
      end;
  end;

  if bottom > 0 then
      if Pos[x][y+1] * multiplier <= 0 then //bc
      begin
        SetLength(help, Length(help)+1);
        help[Length(help)-1] := base + IntToStr(x) + IntToStr(y+1);
      end;

    if y > 0 then
      if Pos[x][y-1] * multiplier <= 0 then //tc
      begin
        SetLength(help, Length(help)+1);
        help[Length(help)-1] := base + IntToStr(x) + IntToStr(y-1);
      end;

  if right > 0 then
  begin
    if bottom > 0 then
      if Pos[x+1][y+1] * multiplier <= 0 then //br
      begin
        SetLength(help, Length(help)+1);
        help[Length(help)-1] := base + IntToStr(x+1) + IntToStr(y+1);
      end;

    if Pos[x+1][y] * multiplier <= 0 then //cr
    begin
      SetLength(help, Length(help)+1);
      help[Length(help)-1] := base + IntToStr(x+1) + IntToStr(y);
    end;

    if y > 0 then
      if Pos[x+1][y-1] * multiplier <= 0 then //tr
      begin
        SetLength(help, Length(help)+1);
        help[Length(help)-1] := base + IntToStr(x+1) + IntToStr(y-1);
      end;
  end;

  result := help;
end;

procedure GetAll(White: Boolean);
var
  multiplier, i, j, n, Len, test: Integer;
  waiting : TArray<String>;
begin
  SetLength(possibleMoves, 0);
  if White then
    multiplier := 1
  else
    multiplier := -1;
  for i := 0 to wdt-1 do
  begin
    for j := hgt-1 downto 0 do
    begin
      test := Pos[i][j] * multiplier;
      case test of
      1: waiting := GetPawn(White, i, j);
      2: waiting := GetKnight(multiplier, i, j);
      3: waiting := GetBishop(multiplier, i, j);
      4: waiting := GetRook(multiplier, i, j);
      5: waiting := GetQueen(multiplier, i, j);
      6: waiting := GetKing(multiplier, i, j)
      else
        waiting := [];
      end;
      Len := Length(possibleMoves);
      SetLength(possibleMoves, Length(possibleMoves)+Length(waiting));
      for n := 0 to Length(waiting)-1 do
        possibleMoves[Len+n] := waiting[n];
    end;
  end;
end;


(*##############################################################################
                             Drawing a given Move
##############################################################################*)


procedure TForm1.DrawMove(moveS : String; leave : Integer);
var
  x1, x2, y1, y2, side, offset : Integer;
  Picture : TPicture;
begin
  x1 := StrToInt(moveS[1]);
  y1 := StrToInt(moveS[2]);
  x2 := StrToInt(moveS[3]);
  y2 := StrToInt(moveS[4]);
  if Big then
    offset := 0
  else
    offset := 1;
  side := (14 - hgt)*8;

  with Image1.Canvas do
  begin
    if (x1 + y1) mod 2 = 1 then
      Brush.Color := StringToColor(clDark)
    else
      Brush.Color := StringToColor(clBright);
    Rectangle(x1*side+offset*32, y1*side, (x1+1)*side+offset*32, (y1+1)*side);

    if (x2 + y2) mod 2 = 1 then
      Brush.Color := StringToColor(clDark)
    else
      Brush.Color := StringToColor(clBright);
    Rectangle(x2*side+offset*32, y2*side, (x2+1)*side+offset*32, (y2+1)*side);

    Picture := TPicture.Create;
    case Pos[x1,y1] of     //♚  ♛  ♝  ♞  ♜  ♟︎ ♙ ♖ ♘ ♗ ♕ ♔
    1: Picture.LoadFromFile('..\Pictures\WP.png');
    2: Picture.LoadFromFile('..\Pictures\WN.png');
    3: Picture.LoadFromFile('..\Pictures\WB.png');
    4: Picture.LoadFromFile('..\Pictures\WR.png');
    5: Picture.LoadFromFile('..\Pictures\WQ.png');
    6: Picture.LoadFromFile('..\Pictures\WK.png');
    -1: Picture.LoadFromFile('..\Pictures\KP.png');
    -2: Picture.LoadFromFile('..\Pictures\KN.png');
    -3: Picture.LoadFromFile('..\Pictures\KB.png');
    -4: Picture.LoadFromFile('..\Pictures\KR.png');
    -5: Picture.LoadFromFile('..\Pictures\KQ.png');
    -6: Picture.LoadFromFile('..\Pictures\KK.png');
    end;
    if NOT (Pos[x1][y1] = 0) then
      Image1.Canvas.Draw(x1*side+offset*40,y1*side+offset*8,Picture.Graphic);

    case Pos[x2,y2] of     //♚  ♛  ♝  ♞  ♜  ♟︎ ♙ ♖ ♘ ♗ ♕ ♔
    1: Picture.LoadFromFile('..\Pictures\WP.png');
    2: Picture.LoadFromFile('..\Pictures\WN.png');
    3: Picture.LoadFromFile('..\Pictures\WB.png');
    4: Picture.LoadFromFile('..\Pictures\WR.png');
    5: Picture.LoadFromFile('..\Pictures\WQ.png');
    6: Picture.LoadFromFile('..\Pictures\WK.png');
    -1: Picture.LoadFromFile('..\Pictures\KP.png');
    -2: Picture.LoadFromFile('..\Pictures\KN.png');
    -3: Picture.LoadFromFile('..\Pictures\KB.png');
    -4: Picture.LoadFromFile('..\Pictures\KR.png');
    -5: Picture.LoadFromFile('..\Pictures\KQ.png');
    -6: Picture.LoadFromFile('..\Pictures\KK.png');
    end;
    if NOT (Pos[x2][y2] = 0) then
      Image1.Canvas.Draw(x2*side+offset*40,y2*side+offset*8,Picture.Graphic);
    Picture.Free;
  end;

  moveAt := moveAt + 1;
  if moveAt mod 2 = 0 then
  begin
    StepLbl.Caption := 'Current Step: K' + IntToStr((moveAt + 1) div 2 );
  end
  else
  begin
    StepLbl.Caption := 'Current Step: W' + IntToStr((moveAt + 1) div 2 );
  end;
end;


(*##############################################################################
                         Deciding Which Moves to Make
##############################################################################*)

function TForm1.MakeMove(moveS : String; leave : Integer; NewElement:Boolean) : String;  //leave is important when backtracking
var
  Piece, x1, x2, y1, y2: Integer; //Piece that is being moved or replaced
  newS : String;
begin
  if NewElement then
  begin
    SetLength(moveList, Length(moveList)+1);
    Piece := Pos[StrToInt(moveS[5])][StrToInt(moveS[6])];    //Piece that is being replaced
    if abs(Piece) = 6 then
      KingAlive := False;
    if Piece >= 0 then
      moveList[Length(moveList)-1] := Copy(moveS, 1, 6) + '+' + IntToStr(abs(Piece))
    else
      moveList[Length(moveList)-1] := Copy(moveS, 1, 6) + IntToStr(Piece);
  end;
  x1 := StrToInt(moveS[3]);
  y1 := StrToInt(moveS[4]);
  x2 := StrToInt(moveS[5]);
  y2 := StrToInt(moveS[6]);

  Piece := StrToInt(Copy(moveS, 1, 2));   //Piece that is being moved
  if ((Piece = 1) and (y2 = 0)) or ((Piece = -1) and (y2 = hgt-1)) then
    Pos[x2][y2] := Piece * 5
  else
    Pos[x2][y2] := Piece;
  if Piece = 6 then
  begin
    wx := x2;
    wy := y2;
  end;
  if Piece = -6 then
  begin
    kx := x2;
    ky := y2;
  end;

  Pos[x1][y1] := leave;

  DrawMove(Copy(moveS, 3, 4), leave);

  newS := '';
  newS := newS + Chr(StrToInt(moveS[3]) + 97);
  newS := newS + IntToStr(hgt-StrToInt(moveS[4]));
  newS := newS + Chr(StrToInt(moveS[5]) + 97);
  newS := newS + IntToStr(hgt-StrToInt(moveS[6]));
  result := Copy(newS, 1, 2) + '-' + Copy(NewS,3,2);
end;

(*  KING KILLING
always the first rule:
If the opponent King can be captured, do so
*)

function TForm1.KingKilling(Reverse: Boolean; Number :Integer; White: Boolean):String;
var
  actual: Array of String;
  i, Len: Integer;
  moveS : String;
begin
  SetLength(actual, 0);
  for i := 0 to Length(possibleMoves)-1 do
  begin
    if White then
    begin
      if (StrToInt(possibleMoves[i][5]) = kx) and (StrToInt(possibleMoves[i][6]) = ky) then
      begin
        SetLength(actual, Length(actual)+1);
        actual[Length(actual)-1] := possibleMoves[i];
      end
    end
    else
      if (StrToInt(possibleMoves[i][5]) = wx) and (StrToInt(possibleMoves[i][6]) = wy) then
      begin
        SetLength(actual, Length(actual)+1);
        actual[Length(actual)-1] := possibleMoves[i];
      end
  end;
  //stuff
  Len := Length(actual);
  if Len > 0 then
  begin
  Number := Number mod Len;
  if Reverse then
    moveS := actual[Len-1-Number]
  else
    moveS := actual[Number];
  result := MakeMove(moveS, 0, True);
  end
  else
    result := '';
end;



(*  THE KING MUST DIE
individual rule:
Move a Piece closer to the opponent King (Taxi-cab distance)
*)

function TForm1.KingDead(Reverse: Boolean; Number :Integer; White: Boolean):String; //Order: previous RNG; Number: Current RNG; White: is it white's turn?
var
  actual: Array of String;
  i, Len, dOld, dNew: Integer;
  moveS : String;
begin
  SetLength(actual, 0);
  for i := 0 to Length(possibleMoves)-1 do
  begin
    if White then
    begin
      dOld := abs(kx - StrToInt(possibleMoves[i][3])) + abs(ky - StrToInt(possibleMoves[i][4]));
      dNew := abs(kx - StrToInt(possibleMoves[i][5])) + abs(ky - StrToInt(possibleMoves[i][6]));
      if dOld > dNew then
      begin
        SetLength(actual, Length(actual)+1);
        actual[Length(actual)-1] := possibleMoves[i];
      end;
    end
    else
    begin
      dOld := abs(wx - StrToInt(possibleMoves[i][3])) + abs(wy - StrToInt(possibleMoves[i][4]));
      dNew := abs(wx - StrToInt(possibleMoves[i][5])) + abs(wy - StrToInt(possibleMoves[i][6]));
      if dOld > dNew then
      begin
        SetLength(actual, Length(actual)+1);
        actual[Length(actual)-1] := possibleMoves[i];
      end;
    end;
  end;
  //stuff
  Len := Length(actual);
  if Len > 0 then
  begin
  Number := Number mod Len;
  if Reverse then
    moveS := actual[Len-1-Number]
  else
    moveS := actual[Number];
  result := MakeMove(moveS, 0, True);
  end
  else
    result := '';
end;



(*  LIGHT SQUARES ARE LAVA
individual rule:
Move a piece from a Light Square to a Dark Square
Otherwise, Move a Piece from a Dark Square to another Dark Square
*)

function TForm1.LightLava(Reverse: Boolean; Number :Integer; White: Boolean):String; //Order: previous RNG; Number: Current RNG; White: is it white's turn?
var
  First, Second: Array of String;
  i, Len: Integer;
  moveS : String;
begin
  SetLength(Second, 0);
  for i := 0 to Length(possibleMoves)-1 do
  begin
    if (StrToInt(possibleMoves[i][5]) + StrToInt(possibleMoves[i][6])) mod 2 = 1 then
    begin
      SetLength(Second, Length(Second)+1);
      Second[Length(Second)-1] := possibleMoves[i];
    end
  end;

  SetLength(First, 0);
  for i := 0 to Length(Second)-1 do
  begin
    if (StrToInt(Second[i][3]) + StrToInt(Second[i][4])) mod 2 = 0 then
    begin
      SetLength(First, Length(First)+1);
      First[Length(First)-1] := Second[i];
    end
  end;

  Len := Length(First);
  if Len > 0 then
  begin
  Number := Number mod Len;
  if Reverse then
    moveS := First[Len-1-Number]
  else
    moveS := First[Number];
    result := MakeMove(moveS, 0, True);
  end
  else
  begin
    Len := Length(Second);
    if Len > 0 then
    begin
    Number := Number mod Len;
    if Reverse then
      moveS := Second[Len-1-Number]
    else
      moveS := Second[Number];
      result := MakeMove(moveS, 0, True);
    end
    else
      result := '';
  end;
end;



(*  DARK SQUARES ARE LAVA
individual rule:
Move a piece from a Dark Square to a Light Square
Otherwise, Move a Piece from a Light Square to another Light Square
*)

function TForm1.DarkLava(Reverse: Boolean; Number :Integer; White: Boolean):String; //Order: previous RNG; Number: Current RNG; White: is it white's turn?
var
  First, Second: Array of String;
  i, Len: Integer;
  moveS : String;
begin
  SetLength(Second, 0);
  result := '';
  for i := 0 to Length(possibleMoves)-1 do
  begin
    if (StrToInt(possibleMoves[i][5]) + StrToInt(possibleMoves[i][6])) mod 2 = 0 then
    begin
      SetLength(Second, Length(Second)+1);
      Second[Length(Second)-1] := possibleMoves[i];
    end
  end;

  SetLength(First, 0);
  for i := 0 to Length(Second)-1 do
  begin
    if (StrToInt(Second[i][3]) + StrToInt(Second[i][4])) mod 2 = 1 then
    begin
      SetLength(First, Length(First)+1);
      First[Length(First)-1] := Second[i];
    end
  end;

  Len := Length(First);
  if Len > 0 then
  begin
  Number := Number mod Len;
  if Reverse then
    moveS := First[Len-1-Number]
  else
    moveS := First[Number];
    result := MakeMove(moveS, 0, True);
  end
  else
  begin
    Len := Length(Second);
    if Len > 0 then
    begin
    Number := Number mod Len;
    if Reverse then
      moveS := Second[Len-1-Number]
    else
      moveS := Second[Number];
      result := MakeMove(moveS, 0, True);
    end;
  end;
end;



(*  MIRROR, MIRROR
individual rule:
Mirror the Last move of your opponent (Small: Point Reflection; Big: Reflection horizontal)
Otherwise, Move the same piece as your opponent
*)

function TForm1.Mirror(Reverse: Boolean; Number :Integer; White: Boolean):String; //Order: previous RNG; Number: Current RNG; White: is it white's turn?
var
  actual: Array of String;
  i, Len, x1, x2, y1, y2: Integer;
  moveS, moveOther, Piece : String;
begin
  moveS := '';
  SetLength(actual, 0);
  if Length(moveList) <> 0 then
  begin
    moveOther := moveList[Length(moveList)-1];
    Piece := moveOther[2];
    for i := 0 to Length(possibleMoves)-1 do
    begin
      if possibleMoves[i][2] = Piece then
      begin
        SetLength(actual, Length(actual)+1);
        actual[Length(actual)-1] := possibleMoves[i];
      end;
    end;
    x1 := StrToInt(moveOther[3]);
    y1 := StrToInt(moveOther[4]);
    x2 := StrToInt(moveOther[5]);
    y2 := StrToInt(moveOther[6]);
  end;


  for i := 0 to Length(actual)-1 do
  begin
    if Big then
    begin
      if ((x1 = StrToInt(actual[i][3])) and (7 - y1 = StrToInt(actual[i][4]))) and ((x2 = StrToInt(actual[i][5])) and (7 - y2 = StrToInt(actual[i][6]))) then
        moveS := actual[i];
    end
    else
    begin
      if ((4 - x1 = StrToInt(actual[i][3])) and (5 - y1 = StrToInt(actual[i][4]))) and ((4 - x2 = StrToInt(actual[i][5])) and (5 - y2 = StrToInt(actual[i][6]))) then
        moveS := actual[i];
    end;
  end;

  Len := Length(actual);
  if (Len > 0) and (moveS = '') then
  begin
    Number := Number mod Len;
    if Reverse then
      moveS := actual[Len-1-Number]
    else
      moveS := actual[Number];
  end;
  if Length(moveS) > 0 then
    result := MakeMove(moveS, 0, True)
  else
    result := '';
end;



(*  LET'S SWITCH SIDES
individual rule:
Move your pieces closer to the setup position of your opponent (Pawns only consider same column)
*)

function TForm1.Switch(Reverse: Boolean; Number :Integer; White: Boolean):String; //Order: previous RNG; Number: Current RNG; White: is it white's turn?
var
  actual: Array of String;
  Places : Array of Array of String;
  i, j, Len, d1, d2, dnew, Piece: Integer;
  moveS,  xgoal, ygoal : String;
begin
  SetLength(actual, 0);
  for i := 0 to Length(possibleMoves)-1 do
  begin
    Piece := StrToInt(Copy(possibleMoves[i], 1, 2));
    if Big then
      case Piece of
      6:  Places := [['4', '0']];
      5:  Places := [['3', '0']];
      4:  Places := [['0', '0'], ['7', '0']];
      3:  Places := [['2', '0'], ['5', '0']];
      2:  Places := [['1', '0'], ['6', '0']];
      1:  Places := [[possibleMoves[i][3], '1']];
      -1: Places := [[possibleMoves[i][3], '6']];
      -2: Places := [['1', '7'], ['6', '7']];
      -3: Places := [['2', '7'], ['5', '7']];
      -4: Places := [['0', '7'], ['7', '7']];
      -5: Places := [['3', '7']];
      -6: Places := [['4', '7']];
      end
    else
      case Piece of
      6:  Places := [['0', '0']];
      5:  Places := [['1', '0']];
      4:  Places := [['4', '0']];
      3:  Places := [['2', '0']];
      2:  Places := [['3', '0']];
      1:  Places := [[possibleMoves[i][3], '1']];
      -1: Places := [[possibleMoves[i][3], '4']];
      -2: Places := [['1', '5']];
      -3: Places := [['2', '5']];
      -4: Places := [['0', '5']];
      -5: Places := [['3', '5']];
      -6: Places := [['4', '5']];
      end;
    d1 := 100;
    for j := 0 to Length(Places)-1 do
    begin
      d2 := abs(StrToInt(possibleMoves[i][3]) - StrToInt(Places[j][0])) + abs(StrToInt(possibleMoves[i][4]) - StrToInt(Places[j][1]));
      if d2 < d1 then
      begin
        xgoal := Places[j][0];
        ygoal := Places[j][1];
        d1 := d2;
      end;
    end;

    dNew := abs(StrToInt(possibleMoves[i][5]) - StrToInt(xgoal)) + abs(StrToInt(possibleMoves[i][6]) - StrToInt(ygoal));
    if dNew < d1 then
    begin
      SetLength(actual, Length(actual)+1);
      actual[Length(actual)-1] := possibleMoves[i];
    end;
  end;



  Len := Length(actual);
  if Len > 0 then
  begin
  Number := Number mod Len;
  if Reverse then
    moveS := actual[Len-1-Number]
  else
    moveS := actual[Number];
  result := MakeMove(moveS, 0, True);
  end
  else
    result := '';
end;



(*  ANY MOVE
always last rule:
Do any possible move
*)

function TForm1.AnyMove(Reverse: Boolean; Number :Integer; White: Boolean):String;
var
  moveS: String;
  Len : Integer; //Piece, remembers type of captured piece (or empty)
begin
  Len := Length(possibleMoves);
  Number := Number mod Len;
  if Reverse then
    moveS := possibleMoves[Len-1-Number]
  else
    moveS := possibleMoves[Number];
  result := MakeMove(moveS, 0, True);
end;

procedure TForm1.AppendPart(Text:String);
var
  last : String;
  len : Integer;
begin
  len := Memo1.Lines.Count-1;
  last := Memo1.Lines[len];
  Memo1.Lines.Delete(len);
  Memo1.Lines.Add(last + Text);
end;

procedure TForm1.CalcBtnClick(Sender: TObject);
var
  WKey, KKey, coords : String; //Keys der Farben mit vorherigem Seed
  moveCount, actualMove, Number : Integer;
  Reverse : Boolean;
begin
  if Big then
    ResetBig()
  else
    ResetSmall();
  case WRNGGroup.ItemIndex of
  0: WKey := Base(WRNGEdt.Text); //Eingabe als Seed + Base Number (akzeptiert Buchstaben die zu A1Z26 werden, getting singular digits)
  1: WKey := Key(WRNGEdt.Text); //Eingabe als Seed + given string (keine weitere Berechnungen), wennzu kurz wird Key wiederholt
  2: WKey := RNG(WRNGEdt.Text); //Generiert 41 zufällige Zahlen, nimmt gesetzten Start an
  end;
  WRNGEdt.Text := WKey;
  WRNGGroup.ItemIndex := 1;
  case KRNGGroup.ItemIndex of
  0: KKey := Base(KRNGEdt.Text); //Eingabe als Seed + Base Number (akzeptiert Buchstaben die zu A1Z26 werden, getting singular digits)
  1: KKey := Key(KRNGEdt.Text); //Eingabe als Seed + given string (keine weitere Berechnungen), wennzu kurz wird Key wiederholt
  2: KKey := RNG(KRNGEdt.Text); //Generiert 41 zufällige Zahlen, nimmt gesetzten Start an
  end;
  KRNGEdt.Text := KKey;
  KRNGGroup.ItemIndex := 1;

  moveAt := 0;
  Memo1.Lines.Clear;
  SetLength(moveList, 0);
  KingAlive := True;
  moveCount := 1;
  while KingAlive and (moveCount < 81) do
  begin
    coords := '';
    actualMove:= (moveCount+1) div 2;
    if moveCount mod 2 = 1 then               //White Move
    begin
      Memo1.Lines.Add(IntToStr(actualMove)+': ');
      if StrToInt(WKey[actualMove]) mod 2 = 0 then
        Reverse := False
      else
        Reverse := True;

      GetAll(True);    //creates public possibleMoves with all possible moves for White
      Number := StrToInt(WKey[actualMove+1]);

      coords := KingKilling(Reverse, Number, True);  //King Killing
      if Length(coords) < 1 then
      begin
        case WTypeGroup.ItemIndex of                //Rule Set
        0:coords := KingDead(Reverse, Number, True);
        1:coords := LightLava(Reverse, Number, True);
        2:coords := DarkLava(Reverse, Number, True);
        3:coords := Mirror(Reverse, Number, True);
        4:coords := Switch(Reverse, Number, True);
        end;
      end;
      if Length(coords) < 1 then
        coords := AnyMove(Reverse, Number, True);   //Any Move
      coords := coords + ' ';
    end
    else                                     //Black Move
    begin
      if StrToInt(KKey[actualMove]) mod 2 = 0 then
        Reverse := False
      else
        Reverse := True;

      GetAll(False);    //creates public possibleMoves with all possible moves for Black
      Number := StrToInt(KKey[actualMove+1]);

      coords := KingKilling(Reverse, Number, False);    //King Killing
      if Length(coords) < 1 then
        case KTypeGroup.ItemIndex of                    //Rule Set
        0:coords := KingDead(Reverse, Number, False);
        1:coords := LightLava(Reverse, Number, False);
        2:coords := DarkLava(Reverse, Number, False);
        3:coords := Mirror(Reverse, Number, False);
        4:coords := Switch(Reverse, Number, False);
        end;
      if Length(coords) < 1 then
        coords := AnyMove(Reverse, Number, False);       //Any Move
    end;
    AppendPart(coords);                    //Add Coordinates
    moveCount := moveCount + 1;
  end;
  if KingAlive then
    Memo1.Lines.Add('Draw: Both kings are alive after 40 moves')
  else
    if moveCount mod 2 = 1 then
      Memo1.Lines.Add('Black Wins')
    else
      Memo1.Lines.Add('White Wins');
  Nextbtn.Enabled := False;
  PrevBtn.Enabled := True;
end;

procedure TForm1.PrevBtnClick(Sender: TObject);
var
  moveS, reverseS : String;
begin
  moveAt := moveAt -2;
  moveS := moveList[moveAt+1];
  reverseS := Copy(moveS, 1, 2);
  reverseS := reverseS + Copy(moveS, 5, 2);
  reverseS := reverseS + Copy(moveS, 3, 2);
  MakeMove(reverseS, StrToInt(Copy(moveS, 7,2)), False);
  NextBtn.Enabled := True;
  if moveAt = 0 then
    PrevBtn.Enabled:= False;
end;

procedure TForm1.NextBtnClick(Sender: TObject);
var
  moveS: String;
begin
  moveS := moveList[moveAt];
  MakeMove(Copy(moveS, 1,6), 0, False);
  PrevBtn.Enabled := True;
  if moveAt = Length(moveList) then
    NextBtn.Enabled:= False;
end;

end.
