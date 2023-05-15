package InterfaceShape;

interface SquareDetails{
    void sidesLength(int sideLength);
    void squareArea(int sideLength);
    void dimensions(int dimension);
}

interface CircleDetails{
    void raidusSize(double raidus);
    void circleArea(double raidus);
}

public abstract class Shape{
    public abstract void shape();
}