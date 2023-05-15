package AbstractShape;

class Square extends Dimensions{
    public Square(int dimensions, int sideSize) {
        super(dimensions,sideSize);
    }
    @Override
    public int CalArea() {
        return(sideSize*sideSize);
    }
    @Override
    public int perimeter(){
        return(4*sideSize);
    }

}

