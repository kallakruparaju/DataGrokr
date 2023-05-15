package InterfaceShape;

public class Square extends Shape implements SquareDetails{
    @Override
    public void shape() {
        System.out.println("The Shape of the object is: "+ getClass().getSimpleName());
    }

    @Override
    public void sidesLength(int sideLength) {
        System.out.println("The Side length of the "+ getClass().getSimpleName()+" is "+sideLength);
    }

    @Override
    public void squareArea(int sideLength) {
        System.out.println("The Area of the "+ getClass().getSimpleName()+" is "+sideLength*sideLength);
    }

    @Override
    public void dimensions(int dimension) {
        System.out.println("The dimensions of the "+ getClass().getSimpleName()+" is "+dimension);
    }
    
}