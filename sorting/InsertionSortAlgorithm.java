import java.util.Random;

/**
Class implement Insertion Sort
Extend documentation about this algorithm can be found here https://en.wikipedia.org/wiki/Insertion_sort

	Pseudocode for insertion sorting algorithm:

		for i ← 1 to length(A)
    	j ← i
    	while j > 0 and A[j-1] > A[j]
        	swap A[j] and A[j-1]
        	j ← j - 1

Analysis:
  - Best case scenario is when input is an array that is already sorted => O(n) (linear running time).
  - Worst case sceneario is when input is an array sorted in reverse order => O(n^2) (quadratic running time).
  - Average case => O(n^2).
*/
public class InsertionSortAlgorithm{
	
	/**
	Method which implements the Insertion sorting algorithm
	*/
	private int[] insertionSort(int[] v){
		int j = 0;
		if(v == null){
			return null;
		}
		else{
			for(int i=1; i < v.length; i++){
				j=i;
				while((j>0)&&(v[j-1] > v[j])){
					v = swap(v, j-1, j);
					j = j - 1;
				}
			}
			return v;
		}	
	}

	/**
	Auxiliary method to swap values from idx1 source index to idx2 target index
	*/
	private int[] swap(int[] v, int idx1, int idx2){
		if(v == null){
			return v;
		}else{
			int aux = v[idx1];
			v[idx1] = v[idx2];
			v[idx2] = aux;
			return v;
		}
	}

	/**
	Main method to launch execution
	*/
	public static void main(String args[]){
		InsertionSortAlgorithm isa = new InsertionSortAlgorithm();

		Random r = new Random();

		int length = r.nextInt(25);
		length = (length > 0 ? length : -length);

		System.out.println("Length: " + length);
		int[] v = new int[length];
		
		System.out.print("vector: {");
		
		for(int i = 0; i < length; i++){
			v[i] = r.nextInt(25);
			v[i] = (v[i] > 0 ? v[i] : -v[i]);
			if(i == length - 1){
				System.out.print(v[i]+"}\n");
			}else{
				System.out.print(v[i]+", ");
			}
			
		}
		v = isa.insertionSort(v);
		System.out.print("Sorted vector: {");
		for(int i = 0; i < length; i++){
			if(i == length - 1){
				System.out.print(v[i]+"}\n");
			}else{
				System.out.print(v[i]+", ");
			}
		}
	}
}