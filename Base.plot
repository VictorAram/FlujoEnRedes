set term pdf
set output 'tarea4.pdf'
set xrange [-0.1:1.1]
set yrange [-0.1:1.1]
set pointsize 1
set size square
set key off
set arrow1 from 0.823607,0.735114 to 0.900000, 0.500000 nohead
set arrow2 from 0.900000,0.500000 to 0.823607, 0.735114 nohead
set arrow3 from 0.623607,0.880423 to 0.823607, 0.735114 nohead
set arrow4 from 0.823607,0.735114 to 0.623607, 0.880423 nohead
set arrow5 from 0.376393,0.880423 to 0.623607, 0.880423 nohead
set arrow6 from 0.623607,0.880423 to 0.376393, 0.880423 nohead
set arrow7 from 0.176393,0.735114 to 0.376393, 0.880423 nohead
set arrow8 from 0.376393,0.880423 to 0.176393, 0.735114 nohead
set arrow9 from 0.100000,0.500000 to 0.176393, 0.735114 nohead
set arrow10 from 0.176393,0.735114 to 0.100000, 0.500000 nohead
set arrow11 from 0.176393,0.264886 to 0.100000, 0.500000 nohead
set arrow12 from 0.100000,0.500000 to 0.176393, 0.264886 nohead
set arrow13 from 0.376393,0.119577 to 0.176393, 0.264886 nohead
set arrow14 from 0.176393,0.264886 to 0.376393, 0.119577 nohead
set arrow15 from 0.623607,0.119577 to 0.376393, 0.119577 nohead
set arrow16 from 0.376393,0.119577 to 0.623607, 0.119577 nohead
set arrow17 from 0.823607,0.264886 to 0.623607, 0.119577 nohead
set arrow18 from 0.623607,0.119577 to 0.823607, 0.264886 nohead
set arrow19 from 0.900000,0.500000 to 0.823607, 0.264886 nohead
set arrow20 from 0.823607,0.264886 to 0.900000, 0.500000 nohead
show arrow
plot 'tarea4.dat' using 1:2 with points pt 7
quit()
