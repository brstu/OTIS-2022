InputStream inputStream = System.in
Reader inputStreamReader = new InputStreamReader(inputStream)
BufferedReader bufferedReader = new BufferedReader(inputStreamReader)

String name = bufferedReader.readLine()
String sAge = bufferedReader.readLine() 
int nAge = Integer.parseInt(sAge)