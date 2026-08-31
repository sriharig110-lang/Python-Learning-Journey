# NumPy Basics

Practice covering core NumPy operations — array creation, indexing/slicing, 
reshaping, and broadcasting.

## Topics covered

- **Array creation** — ranges, zeros/ones, identity matrices, linspace, random arrays
- **Indexing & slicing** — step slicing, sub-array extraction, reversing, boolean indexing
- **Reshaping** — reshape, flatten, transpose
- **Broadcasting** — element-wise operations across different shapes

## Files

- `numpy_practice.ipynb` — hands-on practice + 15 exercises covering array creation, 
  indexing, reshaping, and broadcasting

## Key takeaways

- Broadcasting lets NumPy perform operations on arrays of different shapes 
  without explicit loops, as long as shapes are compatible
- `linspace(start, stop, num)` divides the range into `num-1` equal gaps, 
  not `num` — an easy off-by-one mistake
- Boolean indexing (`arr[arr > 50]`) is a clean way to filter without loops
