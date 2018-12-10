
//problem 1
import java.lang;
import java.io;
import java.System;
import java.util.*;


public class Unchecked_Exception{
	public static void main(String args[]){
		int num[] = {-21, 13, 9, 4, 123};
		try{
			System.out.println(num[6]);
		}

		catch (Exception e){
			Syste.out.println("Error: index out of range");
		}
}



//problem 2
//override
public class Pet{
	private String name;
	private int age;

	public Pet(String name, int age){
		this.name = name;
		this.age = age;
	}


@Override
public boolean equals(Object that){
	if (that instanceof Pet){
		Pet thatPet = (Pet)that;
	}
	return (this.name.equals(thatPet.name)) && (this.age == that.age)
}

}


//problem 3
public class Student{
	private int stdid;
	private String name;

	public Student(int stdid, String name){
		this.stdid = stdid;
		this.name = name;
	}

	public int getID(){
		return this.stdid;
	}

	public int getName(){
		return this.name;
	}
}

public class StudentDriver{
	public static void main(String args[]){
		ArrayList<Student> list = new ArrayList<Student>();
		Student one = new Student("Sydney", 123);
		Student two = new Student("Anna", 432);
		list.add(one);
		list.add(two);

		for (Student std : list){
			System.out.println(std.getID() + " "+std.getName()+" ");
		}
	}
}











