package InterfaceShape;

public class Main {
    public static void main(String[] args) {
        Square square = new Square();
        Shape Squareshape = square;
        SquareDetails squareDetails = square;
        Squareshape.shape();
        squareDetails.dimensions(2);
        squareDetails.squareArea(4);
        squareDetails.sidesLength(4);
        Circle circle = new Circle();
        Shape Circleshape = circle;
        CircleDetails circleDetails = circle;
        Circleshape.shape();
        circleDetails.circleArea(4);
        circleDetails.raidusSize(4);
    }
    
}

