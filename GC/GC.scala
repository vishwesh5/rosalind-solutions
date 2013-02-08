import scala.io._

class Fasta(h: String, n: String) {
  val header: String = h
  val nucleotides : String = n

  def gc_content(): Float = {
    val len : Float = nucleotides.length
    val gc_count : Float = nucleotides.filter(x => x == 'G' || x == 'C').length
    return 100.0f * (gc_count / len)
  }
}

class FastaFactory() {
  def make_fasta(unparsed_string: String) : Fasta = {
    val tokens = unparsed_string.split("\n")
    val header = tokens(0)
    val nucleotides = tokens.drop(1).map(x => x.replace("\n", ""))
    return new Fasta(header, nucleotides.foldLeft("")((x, y) => x + y))
  }
}

object GC {
  def main(args: Array[String]) {
    val data = Source.fromFile("data.txt").mkString.split(">")
    val ff = new FastaFactory()
    val fasta_data = data.drop(1).map(x => ff.make_fasta(x)).sortWith((x, y) => x.gc_content() > y.gc_content())
    println(fasta_data(0).header)
    println(fasta_data(0).gc_content())
  }
}
