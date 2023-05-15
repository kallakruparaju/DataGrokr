package AbstractShape;

class Cube extends Dimensions{
    public Cube(int dimensions,int sideSize) {
        super(dimensions,sideSize);
    }
    @Override
    public int CalArea() {
           return(6*sideSize*sideSize);
    }
    @Override
    public int perimeter(){
        return(12*sideSize);
    }

}

