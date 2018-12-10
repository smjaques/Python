import java.time.LocalTime;

class CourseSection
{
   private final String prefix;
   private final String number;
   private final int enrollment;
   private final LocalTime startTime;
   private final LocalTime endTime;

   public CourseSection(final String prefix, final String number,
      final int enrollment, final LocalTime startTime, final LocalTime endTime)
   {
      this.prefix = prefix;
      this.number = number;
      this.enrollment = enrollment;
      this.startTime = startTime;
      this.endTime = endTime;
   }

   public boolean equals(Object other) {
      if (other == null) {
         return false;
      }
      if (other.getClass() != this.getClass()) {
         return false;
      }
      CourseSection cs = (CourseSection) other;
      return prefix.equals(cs.prefix) &&
              number.equals(cs.number) &&
              enrollment == cs.enrollment &&
              startTime.equals(cs.startTime) &&
              endTime.equals((cs.endTime));
   }




   public int hashCode(){
      return 3 + prefix.hashCode() + number.hashCode() + ((Integer)(enrollment)).hashCode() +
              startTime.hashCode() + endTime.hashCode();
   }

   // additional likely methods not defined since they are not needed for testing
}
