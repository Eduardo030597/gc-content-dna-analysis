def calculate_gc_content(dna_sequence):
    """
    Calculate the GC content of a DNA sequence.
    """
    dna_sequence = dna_sequence.upper()
    g_count = dna_sequence.count('G')
    c_count = dna_sequence.count('C')
    total_length = len(dna_sequence)

    if total_length == 0:
        return 0

    gc_content = ((g_count + c_count) / total_length) * 100
    return gc_content


# Example usage
if __name__ == "__main__":
    sample_sequence = "ATGCGCGTAACCGGTT"
    gc = calculate_gc_content(sample_sequence)
    print(f"GC Content: {gc:.2f}%")
