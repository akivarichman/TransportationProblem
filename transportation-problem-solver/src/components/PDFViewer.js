import React, { useState } from "react";
import { Document, Page } from "react-pdf";
import "react-pdf/dist/esm/Page/AnnotationLayer.css";
import "react-pdf/dist/esm/Page/TextLayer.css";
// import { pdfjs } from "react-pdf";

// // // Set the worker URL
// pdfjs.GlobalWorkerOptions.workerSrc = `//cdnjs.cloudflare.com/ajax/libs/pdf.js/4.8.69/pdf.worker.min.mjs`;


// // import pdfWorker from "react-pdf/node_modules/pdfjs-dist/build/pdf.worker.min.mjs";
// // import pdfWorker from "pdfjs-dist/build/pdf.worker.min.mjs";

// // pdfjs.GlobalWorkerOptions.workerSrc = pdfWorker;

// // pdfjs.GlobalWorkerOptions.workerSrc = 'cdnjs.cloudflare.com/ajax/libs/pdf.js/4.8.69/pdf.worker.min.js';

// // pdfjs.GlobalWorkerOptions.workerSrc = new URL(
// //     pdfWorker,
// //     import.meta.url
// //   ).toString();


function PDFViewer() {
    const [numPages, setNumPages] = useState(null); // Total number of pages in the PDF
    const [currentPage, setCurrentPage] = useState(1); // Currently displayed page

    // Function to handle successful PDF load
    const onDocumentLoadSuccess = ({ numPages }) => {
        setNumPages(numPages);
    };

    // Handlers for navigation
    const goToPrevPage = () => setCurrentPage((prev) => Math.max(prev - 1, 1));
    const goToNextPage = () => setCurrentPage((prev) => Math.min(prev + 1, numPages));

    return (
        <div style={{ textAlign: "center" }}>
            {/* Render PDF document */}
            <Document
                file="/public/Aryeh_Richman_Senior_Thesis.pdf" // Path to your PDF file
                onLoadSuccess={onDocumentLoadSuccess}
            >
                <Page pageNumber={currentPage} />
            </Document>

            {/* Navigation Controls */}
            <div style={{ marginTop: "10px" }}>
                <button onClick={goToPrevPage} disabled={currentPage <= 1}>
                    Previous
                </button>
                <span style={{ margin: "0 15px" }}>
                    Page {currentPage} of {numPages}
                </span>
                <button onClick={goToNextPage} disabled={currentPage >= numPages}>
                    Next
                </button>
            </div>
        </div>
    );
}

export default PDFViewer;
