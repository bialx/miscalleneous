import os,glob,subprocess
from subprocess import check_output
from subprocess import call

NBR_ITER = 5000
field = [79, 83, 89, 97, 101, 107, 113, 127]
operation = ['add', 'mul', 'inv', 'sqr', 'red', 'mul_ur', 'sqr_ur', 'vec_mul']
bib = ['"AVX"', '"MPFQ"', '"NTL"', '"RELIC"', '"C32"']
# , 131, 137 'mul_ur', 'sqr_ur' 131, 137

old_layer = '"AVX"'


#Compilation phase
os.system("mkdir compil")
for layer in bib:
    subprocess.call(['/bin/bash', '-i', '-c', "bclean"])
    with open("CMakeLists.txt", "r") as f:
        data = f.read()
        data = data.replace(f"FFI_LAYER_IMPLEM {old_layer} CACHE STRING", f"FFI_LAYER_IMPLEM {layer} CACHE STRING")

    with open("CMakeLists.txt", 'w') as f:
        f.write(data)
    old_layer = layer
    try:
        subprocess.call(['/bin/bash', '-i', '-c', "bcm"])
    except:
        pass
    compil = (layer.replace('"', "", 2)).lower()
    os.system(f'cp bin/{compil}-* compil/')
os.system(f'cp compil/* bin/')


#Write perf in a tex file
header = r'''\documentclass{article}
\usepackage{array}
\begin{document}
'''
main = ''
footer = r'''\end{document}'''

for m in field:
        main +=  '\\begin{tabular}{|c|c|c|c|c|c|}\hline\multicolumn{6}{|c|}{\\textbf{FIELD =} \\textbf{'+str(m)+r'''}}\\ \hline
'''
        main += r'''OPERATION & MPFQ & AVX & C32 & RELIC & NTL\\ \hline'''
        print(f"CURRENT M = {m}")
        for oper in operation:
            print(f"operation -> {oper}")
            out = str(check_output(["perl", "perf-test.pl", oper, str(m), str(NBR_ITER), ">", "/dev/null"]))
            mpfq = (out.split("MPFQ : ")[1]).split("\\n")[0]
            avx = out.split("AVX  :")[1].split("\\n")[0]
            relic = out.split("RELIC :")[1].split("\\n")[0]
            c32 = out.split("C32  :")[1].split("\\n")[0]
            ntl = out.split("NTL  :")[1].split("\\n")[0]
            main = main + ' $' + f'{oper} $' + ' & ' + str(mpfq) + ' & ' + str(avx) + ' &  ' + str(c32) + ' & '+ str(relic) + ' & ' + str(ntl)
            main += r''' \\ \hline'''

        main += r'''\hline\end{tabular}\newline\vspace*{1cm}\newline'''

content = header + main + footer

with open('perf.tex','w') as f:
     f.write(content)

commandLine = subprocess.Popen(['pdflatex', 'perf.tex'])
commandLine.communicate()

os.unlink('perf.aux')
os.unlink('perf.log')
os.unlink('perf.tex')
os.system("rm -r compil")
