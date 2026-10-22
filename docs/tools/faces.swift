import Vision
import AppKit
for path in CommandLine.arguments.dropFirst() {
  guard let img = NSImage(contentsOfFile: path), let cg = img.cgImage(forProposedRect: nil, context: nil, hints: nil) else { print(path, "load fail"); continue }
  let req = VNDetectFaceRectanglesRequest()
  try? VNImageRequestHandler(cgImage: cg, options: [:]).perform([req])
  let W = Double(cg.width), H = Double(cg.height)
  for f in (req.results ?? []) { let b = f.boundingBox
    print(String(format: "%@ %dx%d face cx=%.0f cy=%.0f w=%.0f h=%.0f", (path as NSString).lastPathComponent, cg.width, cg.height, (b.midX)*W, (1-b.midY)*H, b.width*W, b.height*H)) }
}
