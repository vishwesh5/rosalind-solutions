import scala.io._
import scala.collection.mutable.ArrayBuffer

class Fasta(h: String, n: String) {
  val header: String = h
  val nucleotides : String = n

  def gc_content(): Float = {
    val len : Float = nucleotides.length
    val gc_count : Float = nucleotides.filter(x => x == 'G' || x == 'C').length
    return 100.0f * (gc_count / len)
  }

  def overlap_graph_exists(f: Fasta, k: Int) : Boolean = {
    val w = f.nucleotides.substring(0, k)
    return nucleotides.endsWith(w)
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

object GRPH {

  var am: ArrayBuffer[String] = new ArrayBuffer()

  def try_add(x: Fasta, y: Fasta) {
    if (x.overlap_graph_exists(y, 3)) {
        val entry = x.header + " " + y.header
        if (!am.contains(entry)) {
          am += entry
        }
      }
  }

  def construct_adjacency_matrix(f: Array[Fasta], idx: Int) : Unit = {
    val len = f.length
    if (idx == len) return
    val right = f.drop(idx+1)
    val current = f(idx)
    val left = f.slice(0, idx)
    right.map(x => try_add(x, current))
    left.map(x => try_add(x, current))
    construct_adjacency_matrix(f, idx+1)
  }

  def main(args: Array[String]) {
    val data = Source.fromFile("data.txt").mkString.split(">")
    val ff = new FastaFactory()
    val fasta_data = data.drop(1).map(x => ff.make_fasta(x))
    construct_adjacency_matrix(fasta_data, 0)
    am.map(x => println(x))
  }
}
