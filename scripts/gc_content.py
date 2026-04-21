def calculate_gc_content(dna_sequence):
    """
    Calculate the GC content of a DNA sequence.
    """
    dna_sequence = dna_sequence.upper().strip()
    g_count = dna_sequence.count("G")
    c_count = dna_sequence.count("C")
    total_length = len(dna_sequence)

    if total_length == 0:
        return 0

    gc_content = ((g_count + c_count) / total_length) * 100
    return gc_content


def read_sequence_from_file(file_path):
    """
    Read a DNA sequence from a text file.
    """
    with open(file_path, "r") as file:
        sequence = file.read().strip()
    return sequence


if __name__ == "__main__":
    file_path = "data/example_sequence.txt"
    sample_sequence = read_sequence_from_file(file_path)
    gc = calculate_gc_content(sample_sequence)
    print(f"DNA sequence: {sample_sequence}")
    print(f"GC Content: {gc:.2f}%")
