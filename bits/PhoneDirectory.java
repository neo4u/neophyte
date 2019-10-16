import java.util.BitSet;

class PhoneDirectory{
    private BitSet bitset;
    private int maxNumbers;
    private int currentLeastIndex;
    
    public PhoneDirectory(int maxNumbers){
        this. bitset = new BitSet(maxNumbers);
        this.maxNumbers=maxNumbers;
        this.currentLeastIndex=0;
    }
    
    /** Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available. */
    public int get(){
        if(currentLeastIndex == maxNumbers) return -1;
        
        int index=currentLeastIndex;
        bitset.set(currentLeastIndex);
        currentLeastIndex=bitset.nextClearBit(currentLeastIndex);
        return index;
    }
    
    /** Check if a number is available or not. */
    public boolean check(int number){
        return !bitset.get(number);
    }
    
    /** Recycle or release a number. */
    public void release(int number){
        if(number<currentLeastIndex) currentLeastIndex=number;
        bitset.clear(number);
    }

    public static void main(String args[]){
        PhoneDirectory dir = new PhoneDirectory(3);
        assert dir.get() == 0;
        assert dir.get() == 1;
        assert dir.check(2) == true;
        assert dir.get() == 2;
        assert dir.check(2) == false;
        dir.release(2);
        assert dir.check(2) == true;
    }
}


class PhoneDirectory {
    private BitSet bitmap;
    private int maxNumber;
    /** Initialize your data structure here
        @param maxNumbers - The maximum numbers that can be stored in the phone directory. */
    public PhoneDirectory(int maxNumbers) {
        this.maxNumber = maxNumbers;
        this.bitmap = new BitSet(maxNumbers*2-1);
    }
    
    /** Provide a number which is not assigned to anyone.
        @return - Return an available number. Return -1 if none is available. */
    public int get() {
        int left = 0, right = maxNumber-1;
        int start = 0;
        if(bitmap.get(start)) return -1;
        while(left < right){
            int mid = left + ((right - left) >> 1);
            if(!bitmap.get(start*2+1)){
                start = start*2+1;
                right = mid;
            }
            else{
                start = start*2+2;
                left = mid+1;
            }
        }
        
        flip(left);
       // print();
        return left;
    }
    
    /** Check if a number is available or not. */
    public boolean check(int number) {
        return getStatus(number,0,0,maxNumber-1);
    }
    
    private boolean getStatus(int number, int current, int left, int right){
        if(bitmap.get(current)) return false;
        if(left == right) return !bitmap.get(current);
        int mid = left + ((right-left)>>1);
        if(mid <number){
            return getStatus(number,current*2+2,mid+1,right);
        }else{
            return getStatus(number,current*2+1,left,mid);
        }
        
    }
    private void flip(int number){
        setStatus(number, 0, 0, maxNumber-1);
    }
    private void setStatus(int number, int cur, int left, int right){
        if(left == right){
            bitmap.flip(cur);
            return ;
        }
        int mid = left + ((right-left)>>1);
        if(mid >= number){
            setStatus(number,cur*2+1,left,mid);
        }else{
            setStatus(number,cur*2+2,mid+1,right);
        }
        if(bitmap.get(cur*2+1) && bitmap.get(cur*2+2))
            bitmap.set(cur);
        else{
            bitmap.clear(cur);
        }
    }
    
    
    /** Recycle or release a number. */
    public void release(int number) {
        if(number>=maxNumber || number <0) return;
        if(!check(number)){
            flip(number);
        }
    }

    public static void main(String args[]){
        PhoneDirectory dir = new PhoneDirectory(3);
        assert dir.get() == 0;
        assert dir.get() == 1;
        assert dir.check(2) == true;
        assert dir.get() == 2;
        assert dir.check(2) == false;
        dir.release(2);
        assert dir.check(2) == true;
    }
}
// Leverage the idea of segment tree. get(), check(), release() using O(lg(maxNumbers)), space using O(maxNumbers).