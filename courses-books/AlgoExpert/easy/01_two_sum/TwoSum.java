import java.util.*;

public class TwoSum {

    // O(n) time | O(n) space
    public static int[] twoSum(int[] array, int target) {
        HashMap<Integer, Integer> temp = new HashMap<>();

        for (int number : array) {
            int gift = target - number;

            if (temp.containsKey(gift)) {
                return new int[]{gift, number};
            } else {
                temp.put(number, 1);
            }
        }

        return null;
    }

    // O(n log n) time | O(1) space
    public static int[] twoSum2(int[] array, int target) {
        Arrays.sort(array);

        int L = 0;
        int R = array.length - 1;

        while (L < R) {
            int currentSum = array[L] + array[R];

            if (currentSum < target) {
                L++;
            } else if (currentSum > target) {
                R--;
            } else {
                return new int[]{array[L], array[R]};
            }
        }

        return null;
    }

    // O(n^2) time | O(1) space
    public static int[] twoSum3(int[] array, int target) {

        for (int i = 0; i < array.length; i++) {
            for (int j = i + 1; j < array.length; j++) {
                if (array[i] + array[j] == target) {
                    return new int[]{array[i], array[j]};
                }

            }
        }

        return null;
    }

    public static int[] twoSum4(int[] array, int target) {
       
        return null;
    }



    public static void main(String[] args) {

        int[] arr = {1,6,2,5,8,-3};

        System.out.println(Arrays.toString(twoSum(arr, 10)));
        System.out.println(Arrays.toString(twoSum2(arr, 10)));
        System.out.println(Arrays.toString(twoSum3(arr, 10)));
        System.out.println(Arrays.toString(twoSum4(arr, 10)));
    }
}
