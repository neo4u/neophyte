import java.io.*;
import java.util.*;

/**
* NASA selects Dropbox as its official partner, and we’re tasked with managing
* a panorama for the universe. The Hubble telescope (or some other voyager we
* have out there) will occasionally snap a photo of a sector of the universe,
* and transmit it to us. You are to help write a data structure to manage this.
* For the purpose of this problem, assume that the observable universe has been
* divided into 2D sectors. Sectors are indexed by x- and y-coordinates.
*/
public File {
    public File(String path) {}
    public Boolean exists() {}
    public byte[] read() {}
    public void write(bytes[] bytes) {}
}

public Image {
    public Image(byte[] bytes) {}
    byte[] getBytes() {} // no more than 1MB in size
}

public Sector { 
    public Sector(int x, int y) {}
    int getX() {}
    int getY() {}

    @Override
    public boolean equals(Object o) {
        if(o==this) return true;

        if(!(o instanceof Sector)){
            return false;
        }

        Sector that = (Sector) o;

        return this.x == that.getX() && this.y == that.getY();
    }

    @Override
    public int hashCode() {
        int prime = 31;
        int result = 1;
        result = prime*result + this.x;
        result = prime*result + this.y;
        return result;
    }
}

    /**
    * row-major indexing to be consistent.
    */
    public void removeHead() {
        locMap.put(head.next.key, null);
        head.next = head.next.next;
        head.next.prev = head;
    }
    
    public void addTail(int key, int value) {
        DLinkedList newEle = new DLinkedList(key, value);
        moveToTail(newEle);
        locMap.put(key, newEle);
    }
    
    public void moveToTail(DLinkedList e) {
        e.prev = tail.prev;
        tail.prev.next = e;
        tail.prev = e;
        e.next = tail;
    }
}

// LRU
class LRUCache {
    private int capacity;
    private LinkedHashMap<Integer, Integer> leastRecentUsedList;
    
    public LRUCache(int capacity) {
        this.capacity = capacity;
        leastRecentUsedList = new LinkedHashMap<>();
    }
    
    public int get(int key) {
        if(leastRecentUsedList.containsKey(key)) {
            int value = leastRecentUsedList.get(key);
            leastRecentUsedList.remove(key);
            leastRecentUsedList.put(key, value);
            return value;
        }
        
        return -1;

    }
    
    public void put(int key, int value) {
        if(leastRecentUsedList.containsKey(key)) {
            leastRecentUsedList.remove(key);
        } else if(leastRecentUsedList.size()==capacity) {
            leastRecentUsedList.remove(leastRecentUsedList.keySet().iterator().next());
        }
        leastRecentUsedList.put(key, value);
    }
    
   
}
/*class LRUCache {
    class DLinkedList {
        int key, val;
        DLinkedList prev, next;
        
        public DLinkedList(int _key, int _val) {
            key = _key; val = _val;
        }
    }
    
    private int capacity, count = 0;
    private DLinkedList head, tail;
    private Map<Integer, DLinkedList> locMap = new HashMap<Integer, DLinkedList>();
    
    public LRUCache(int capacity) {
        this.capacity = capacity;
        head = new DLinkedList(-1, -1);//dummy for easier pointer manipulation
        tail = new DLinkedList(-1, -1);
        head.next = tail;
        tail.prev = head;
    }
    
    public int get(int key) {
        DLinkedList e = getNode(key);
        return  e == null? -1: e.val;
    }
    
    public DLinkedList getNode(int key) {
        if(locMap.get(key)!=null) {
            DLinkedList e = locMap.get(key);
            e.next.prev = e.prev;
            e.prev.next = e.next;
            moveToTail(e);
            return e;
        } else {
            return null;
        }
    }
    
    public void put(int key, int value) {
        DLinkedList e = getNode(key);
        if(e!=null) {
           e.val = value;
        } else {
            if(count==capacity) { // remove LRU
                removeHead();
            }
            addTail(key, value);
            count++;
        }

    }
    
    public void removeHead() {
        locMap.put(head.next.key, null);
        head.next = head.next.next;
        head.next.prev = head;
        count--;
    }
    
    public void addTail(int key, int value) {
        DLinkedList newEle = new DLinkedList(key, value);
        moveToTail(newEle);
        locMap.put(key, newEle);
    }
    
    public void moveToTail(DLinkedList e) {
        e.prev = tail.prev;
        tail.prev.next = e;
        tail.prev = e;
        e.next = tail;
    }
}*/

/**
 * Your LRUCache object will be instantiated and called as such:
 * LRUCache obj = new LRUCache(capacity);
 * int param_1 = obj.get(key);
 * obj.put(key,value);
 */