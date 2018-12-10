import java.util.List;
import java.util.Objects;

class Student
{
   private final String surname;
   private final String givenName;
   private final int age;
   private final List<CourseSection> currentCourses;

   public Student(final String surname, final String givenName, final int age,
      final List<CourseSection> currentCourses)
   {
      this.surname = surname;
      this.givenName = givenName;
      this.age = age;
      this.currentCourses = currentCourses;
   }

   public String getSurname(){
      return surname;
   }

   public String getGivenName(){
      return givenName;
   }

   public int getAge(){
      return age;
   }

   public List<CourseSection> getCurrentCourses(){
      return currentCourses;
   }

   public boolean equals(Object other) {
      if (other == null) {
         return false;
      }
      if (other.getClass() != this.getClass()) {
         return false;
      }
      Student s2 = (Student) other;
      return age == s2.age && surname.equals(s2.surname) &&
              givenName.equals(s2.givenName) && currentCourses.equals(s2.currentCourses);
   }


   public int hashCode(){
         return Objects.hash(surname, givenName, age, currentCourses);
      }


}
