class CharacterSet:
    h: str
    v: str
    tl: str
    tr: str
    bl: str
    br: str
    fr: str
    fl: str
    fd: str
    fu: str

    def __init__(
        self,
        h: str,
        v: str,
        tl: str,
        tr: str,
        bl: str,
        br: str,
        fr: str,
        fl: str,
        fd: str,
        fu: str,
    ) -> None:
        self.h = h
        self.v = v
        self.tl = tl
        self.tr = tr
        self.bl = bl
        self.br = br
        self.fr = fr
        self.fl = fl
        self.fd = fd
        self.fu = fu


THIN_H = "\u2500"
THIN_V = "\u2502"
THIN_TL = "\u250c"
THIN_TR = "\u2510"
THIN_BL = "\u2514"
THIN_BR = "\u2518"
THIN_H_DASHED = "\u254c"
THIN_V_DASHED = "\u254e"
THIN_TL_ROUNDED = "\u256d"
THIN_TR_ROUNDED = "\u256e"
THIN_BR_ROUNDED = "\u256f"
THIN_BL_ROUNDED = "\u2570"
THIN_FR = "\u251c"
THIN_FL = "\u2524"
THIN_FD = "\u252c"
THIN_FU = "\u2534"

THICK_H = "\u2501"
THICK_V = "\u2503"
THICK_TL = "\u250f"
THICK_TR = "\u2513"
THICK_BL = "\u2517"
THICK_BR = "\u251b"
THICK_FR = "\u2523"
THICK_FL = "\u252b"
THICK_FD = "\u2533"
THICK_FU = "\u253b"

THIN_MAPPING = CharacterSet(
    h=THIN_H,
    v=THIN_V,
    tl=THIN_TL,
    tr=THIN_TR,
    bl=THIN_BL,
    br=THIN_BR,
    fr=THIN_FR,
    fl=THIN_FL,
    fd=THIN_FD,
    fu=THIN_FU,
)
THIN_ROUNDED_MAPPING = CharacterSet(
    h=THIN_H,
    v=THIN_V,
    tl=THIN_TL_ROUNDED,
    tr=THIN_TR_ROUNDED,
    bl=THIN_BL_ROUNDED,
    br=THIN_BR_ROUNDED,
    fr=THIN_FR,
    fl=THIN_FL,
    fd=THIN_FD,
    fu=THIN_FU,
)
THIN_DASHED_MAPPING = CharacterSet(
    h=THIN_H_DASHED,
    v=THIN_V_DASHED,
    tl=THIN_TL,
    tr=THIN_TR,
    bl=THIN_BL,
    br=THIN_BR,
    fr=THIN_FR,
    fl=THIN_FL,
    fd=THIN_FD,
    fu=THIN_FU,
)
THICK_MAPPING = CharacterSet(
    h=THICK_H,
    v=THICK_V,
    tl=THICK_TL,
    tr=THICK_TR,
    bl=THICK_BL,
    br=THICK_BR,
    fr=THICK_FR,
    fl=THICK_FL,
    fd=THICK_FD,
    fu=THICK_FU,
)
