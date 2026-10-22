import Vision
import CoreImage
import AppKit
let inPath = CommandLine.arguments[1], outPath = CommandLine.arguments[2]
let img = NSImage(contentsOfFile: inPath)!
let cg = img.cgImage(forProposedRect: nil, context: nil, hints: nil)!
let req = VNGeneratePersonSegmentationRequest()
req.qualityLevel = .accurate
req.outputPixelFormat = kCVPixelFormatType_OneComponent8
try VNImageRequestHandler(cgImage: cg, options: [:]).perform([req])
let mask = req.results!.first!.pixelBuffer
var maskCI = CIImage(cvPixelBuffer: mask)
let src = CIImage(cgImage: cg)
maskCI = maskCI.transformed(by: CGAffineTransform(scaleX: src.extent.width / maskCI.extent.width, y: src.extent.height / maskCI.extent.height))
let clear = CIImage(color: .clear).cropped(to: src.extent)
let out = src.applyingFilter("CIBlendWithMask", parameters: [kCIInputBackgroundImageKey: clear, kCIInputMaskImageKey: maskCI])
let ctx = CIContext()
try ctx.writePNGRepresentation(of: out, to: URL(fileURLWithPath: outPath), format: .RGBA8, colorSpace: CGColorSpace(name: CGColorSpace.sRGB)!)
print("ok", Int(maskCI.extent.width), Int(maskCI.extent.height))
