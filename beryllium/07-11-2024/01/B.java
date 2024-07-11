import java.util.*;
import java.security.MessageDigest;

public class B {
    private List<Block> chain;

    public B() {
        this.chain = new ArrayList<>();
        addBlock(new Block("Genesis Block", "0"));
    }

    public void addBlock(Block newBlock) {
        newBlock.previousHash = getLatestBlock().hash;
        newBlock.mineBlock();
        chain.add(newBlock);
    }

    public Block getLatestBlock() {
        return chain.get(chain.size() - 1);
    }

    public boolean isChainValid() {
        for (int i = 1; i < chain.size(); i++) {
            Block currentBlock = chain.get(i);
            Block previousBlock = chain.get(i - 1);
            // compare registered hash and calculated hash
            if (!currentBlock.hash.equals(currentBlock.calculateHash())) {
                System.out.println("Current Block hash is invalid.");
                return false;
            }
            // compare previous hash and registered previous hash
            if (!currentBlock.previousHash.equals(previousBlock.hash)) {
                System.out.println("Previous Block hash is invalid.");
                return false;
            }
        }
        return true;
    }

    public static void main(String[] args) {
        B B = new B();
        B.addBlock(new Block("Send 10 BTC to Alice", ""));
        B.addBlock(new Block("Send 5 BTC to Bob", ""));

        System.out.println("B Valid: " + B.isChainValid());

        // Let's try to tamper a block and see if it gets detected
        Block secondBlock = B.chain.get(1);
        secondBlock.data = "Send 100 BTC to Charlie";
        secondBlock.mineBlock();

        System.out.println("\nB Valid After Tampering: " +
                B.isChainValid());
    }

    // inner class block
    static class Block {
        String data;
        String hash;
        String previousHash;

        Block(String data, String previousHash) {
            this.data = data;
            this.previousHash = previousHash;
        }

        void mineBlock() {
            String guess = this.data + this.previousHash;
            this.hash = calculateHash(guess);
        }

        String calculateHash(String data) {
            try {
                MessageDigest digest = MessageDigest.getInstance("SHA-256");
                byte[] encodedhash = digest.digest(data.getBytes());
                return new String(encodedhash);
            } catch (Exception e) {
                throw new RuntimeException(e);
            }
        }
    }
}