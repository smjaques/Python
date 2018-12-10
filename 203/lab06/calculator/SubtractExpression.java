class SubtractExpression extends BinaryExpression
{
   //private final Expression lft;
   //private final Expression rht;
   private static final String operator = "-";

   public SubtractExpression(final Expression lft, final Expression rht)
   {
      super(lft, rht, operator);
   }

   protected double _applyOperator(double val1, double val2)
   {
      return val1 - val2;
   }
}
