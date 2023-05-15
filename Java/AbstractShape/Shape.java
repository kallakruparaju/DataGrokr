package AbstractShape;

abstract class Dimensions extends Shape{
    public Dimensions(int dimensions, int sideSize) {
        super(dimensions, sideSize);
    }

    @Override
    public int CalArea() {
        if (dimensions == 2) {
            
           return(sideSize*sideSize);
        } else {
            return(6*sideSize*sideSize);
        }
    }
    public abstract int perimeter(); 
} 

public abstract class Shape {
    protected int dimensions;
    protected int sideSize;
    public Shape(int dimensions,int sideSize){
        this.dimensions = dimensions;
        this.sideSize = sideSize;
    }
    public abstract int CalArea();
}
