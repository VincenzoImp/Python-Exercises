

D='12345678901234567890123456789012345678901234567890'
E='abcdefghijklmnopqrstuvwzyzabcdefghijklmnopqrstuvwzyz'
F=$E$F
G='ABCDEFGHIJKLMNOPQRSTUVWXYZABCDEFGHIJKLMNOPQRSTUVWXYZ'

mkdir -p $D/$E/$D/$E/$G
mkdir -p $D/$D/$D/$E/$G
mkdir -p $D/$F/$G/$E/$F
mkdir -p $D/$G/$D/$G/$F
mkdir -p $D/$E/$D/$E/$F
mkdir -p $D/$F/$G/$E/$G
mkdir -p $D/$E/$F/$E/$F

