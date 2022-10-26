set terminal X11 noenhanced
set title "3.5"
set xlabel "s"
set ylabel "V"
set grid
unset logscale x 
set xrange [1.000000e-13:1.000000e-05]
unset logscale y 
set yrange [6.335002e-01:1.363167e+00]
#set xtics 1
#set x2tics 1
#set ytics 1
#set y2tics 1
set format y "%g"
set format x "%g"
plot '../figs/3.5.data' using 1:2 with lines lw 1 title "v(x)"
