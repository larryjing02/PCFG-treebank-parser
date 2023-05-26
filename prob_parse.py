import matplotlib.pyplot as plt

def get_frequencies(filename, elements):
    with open(filename, "r") as f:
        lines = f.readlines()

    tot = len(lines)

    freq_table = {}
    for line in lines:
        line = line.strip()
        line = line[:line.index("=>")].strip()
        freq_table[line] = freq_table.get(line, 0) + 1

    freq_percent = []
    for element in elements:
        freq = freq_table[element] / tot
        freq_percent.append(freq)
        print(f"{filename}: {element} -> {freq}")

    return freq_percent

elements = ["subjh", "extracomp", "nadj_rc", "extradj_i_vp", "frag_np", "imper"]

# Get frequencies for each file
ecoc_freqs = get_frequencies("data/ecoc-pref.txt", elements)
vm_freqs = get_frequencies("data/vm-pref.txt", elements)

# Create bar chart
bar_width = 0.35

plt.figure(figsize=(10, 5))
print(ecoc_freqs)
print(vm_freqs)
for i in range(len(elements)):
    plt.bar(i, ecoc_freqs[i], bar_width, color='purple')
    plt.bar(i + bar_width, vm_freqs[i], bar_width, color='gold')

plt.xlabel('Elements')
plt.ylabel('Probability')
plt.title('Probability of Target Elements')
plt.xticks([r + bar_width / 2 for r in range(len(elements))], elements)
plt.legend(['ecoc-pref.txt', 'vm-pref.txt'])

plt.tight_layout()
plt.show()
