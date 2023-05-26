def get_frequencies(filename, elements):
    with open(filename, "r") as f:
        lines = f.readlines()

    element_set = set(elements)

    table = {}
    for line in lines:
        line = line.strip()
        loc = line.index("=>")
        element = line[:loc].strip()
        if element in element_set:
            rewrite = line[loc+2:].strip()
            if element in table:
                table[element][rewrite] = table[element].get(rewrite, 0) + 1
            else:
                table[element] = {rewrite : 1}
    print(f"Rewrite possibilities for elements in {filename}: ")
    for element in elements:
        freq_table = table[element]
        tot = sum(freq_table.values())
        temp = []
        for rewrite in freq_table:
            temp.append((freq_table[rewrite], f"\t{element} -> {rewrite} [{round(freq_table[rewrite] / tot, 5)}]"))
        # Sort temp by val
        temp = sorted(temp, key=lambda x: -x[0])
        output = [x[1] for x in temp]
        for val in output:
            print(val)
        print()

    return table, len(lines)

elements = ["subjh", "extracomp", "nadj_rc", "extradj_i_vp", "frag_np", "imper"]

# Get frequencies for each file
ecoc_freqs, len_e = get_frequencies("data/ecoc-pref.txt", elements)
vm_freqs, len_v = get_frequencies("data/vm-pref.txt", elements)


for element in elements:
    freq_a = ecoc_freqs[element]
    freq_b = vm_freqs[element]
    greatest_disparity = float('-inf')
    keys_with_greatest_disparity = []
    total_disparity = 0
    
    total_freq_a = sum(freq_a.values())
    total_freq_b = sum(freq_b.values())
    all_keys = set(freq_a.keys()).union(freq_b.keys())

    for key in all_keys:
        freq_a_val = freq_a.get(key, 0) / total_freq_a if total_freq_a > 0 else 0
        freq_b_val = freq_b.get(key, 0) / total_freq_b if total_freq_b > 0 else 0

        disparity = abs(freq_a_val - freq_b_val)
        
        if disparity > greatest_disparity:
            greatest_disparity = disparity
            keys_with_greatest_disparity = [key]
        elif disparity == greatest_disparity:
            keys_with_greatest_disparity.append(key)
        total_disparity += disparity

    print("Disparity Calculation:")
    # Print out rewrite possibility with greatest difference
    print(f"Element \"{element}\": {keys_with_greatest_disparity} with a difference of {greatest_disparity}")
    print(f"\t{element} had a total disparity of {total_disparity}")
    # Print out relative frequency of element
    print(f"\tEmail: {total_freq_a / len_e}\tSpoken: {total_freq_b / len_v}")
