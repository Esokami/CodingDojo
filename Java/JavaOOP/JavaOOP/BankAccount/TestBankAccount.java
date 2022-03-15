public class TestBankAccount {
    public static void main(String[] args){
        BankAccount account1 = new BankAccount();
        account1.depositMoney(20, "Checking");
        account1.withdrawMoney(50, "Savings");
        account1.depositMoney(100, "Savings");
        account1.withdrawMoney(5, "Checking");
        account1.totalBalance();
    }
}
