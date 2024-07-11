import java.util.ArrayList;
import java.util.List;
import java.util.Objects;

class Block {
  private String data;
  private String previousHash;
  private String hash;
  
  public Block(String data, String previousHash) {
    this.data = data;
    this.previousHash = previousHash;
    this.hash = calculateHash();
  }

  public String getData() {
    return data;
  }

  public String getPreviousHash() {
    return previousHash;
  }

  public String getHash() {
    return hash;
  }
  
  private String calculateHash() {
    // Simple SHA-256 based hash calculation (using toString() to represent the block)
    return String.valueOf(Objects.hash(data, previousHash)).substring(0, 10);
  }
}

public class A {
  private List<Block> chain;
  private String currentHash;
  
  public A() {
    this.chain = new ArrayList<>();
    // Add the genesis block to the chain
    this.addBlock("Genesis Block", "0");
  }
  
  public void addBlock(String data) {
    Block newBlock = new Block(data, currentHash);
    chain.add(newBlock);
    currentHash = newBlock.getHash();
  }
  
  public boolean isChainValid() {
    for (int i = 1; i < chain.size(); i++) {
        Block currentBlock = chain.get(i);
        Block previousBlock = chain.get(i-1);
      
        if (!currentBlock.getPreviousHash().equals(previousBlock.getHash())) {
            return false;
        }

        if (!currentBlock.getHash().equals(currentBlock.calculateHash())) {
            return false;
        }
    }
    return true;
  }
  
  // Display the blockchain
  public void printChain() {
    System.out.println("Current Blockchain:");
    for (Block block : chain) {
        System.out.printf("Block: %s%n", block.getData());
        System.out.printf("  Hash: %s%n", block.getHash());
        System.out.printf("  Previous Hash: %s%n", block.getPreviousHash());
    }
  }
  
  public static void main(String[] args) {
      A blockchain = new A();
        
    // Sample transactions 
    blockchain.addBlock("Send 10 BTC to Alice");
    blockchain.addBlock("Send 5 BTC to Bob");
    blockchain.addBlock("Send 2 BTC to Charlie");

    System.out.println("\nBlockchain validity: " + blockchain.isChainValid());
    blockchain.printChain();
  } 
}