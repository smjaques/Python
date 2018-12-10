public class View{
   private String productID;
   private int price;

   public View(String productID, int price){
      this.productID = productID;
      this.price = price;
   }
   public String getProductID(){
      return productID;
   }
   public int getPrice(){
      return price;
   }
}

