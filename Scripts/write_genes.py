import sys
gene_file=sys.argv[1]
out_file = sys.argv[2]
with open (gene_file, 'r') as humchr:
    with open(out_file, 'w')as gene_names:       
        tag = False
        gene_list=[]
        for line in humchr:
            if line.startswith('Gene'):
                    tag = True
            if tag:
                line_split = line.split()
                if len(line_split) != 0:
                    if'_' in line_split[0]:
                        continue
                    else:
                        gene_list.append(line_split[0])
                        #print(gene_list)
        for gene in (gene_list[3:][:-2]):
            gene_names.writelines(gene+'\n')
            