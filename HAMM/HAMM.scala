import scala.io._
object HAMM {
  def main(args: Array[String]) {
    val data = Source.fromFile("data.txt").mkString.split("\n")
    val s = data(0).toCharArray
    val t = data(1).toCharArray
    println((s, t).zipped.toList.map(x => if (x._1 == x._2) 0 else 1).reduceLeft(_ + _))
  }
}
