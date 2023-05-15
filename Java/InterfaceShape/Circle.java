package InterfaceShape;

public class Circle extends Shape implements CircleDetails{

    @Override
    public void raidusSize(double raidus) {
        System.out.println("The raidus length of the "+ getClass().getSimpleName()+" is "+raidus);
    }

    @Override
    public void circleArea(double raidus) {
        System.out.println("The Area of the "+ getClass().getSimpleName()+" is "+ 2 * 2.17 * raidus * raidus);
    }

    @Override
    public void shape() {
        System.out.println("The Shape of the object is: "+ getClass().getSimpleName());
    }

    
}
